# @Controller, @RestController 차이



Spring에서 컨트롤러를 지정해주기 위한 어노테이션들이다.



##### @Controller

- 전통적인 Spring MVC의 컨트롤러



##### @RestController

- Restful 웹서비스의 컨트롤러



두개의 가장 큰 차이는 HTTP Response Body가 생성되는 방식이다.





#### @Controller (Spring MVC Controller)

###### [Controller - View]

주로 view를 반환받기위해 사용되었다.

```java
@Controller
@RequestMapping("/apt")
public class HouseController {
	
	@Autowired
	private HouseService houseService; // 휴,,,,
	
	PageNavigation pageNavigation;
	private List<HouseDeal> list;
	
	@RequestMapping("detail")
	private String detail(int no, Model model) {
		model.addAttribute("detailDeal", houseService.searchByNo(no));
		model.addAttribute("navigation", pageNavigation);
		model.addAttribute("searchType", searchType);
		model.addAttribute("list", list);
		return "apt/aptSearch";
	}
}


```

[코드출처 : 나](https://github.com/oheong/HappyHouse_back-end/blob/master/src/main/java/com/ssafy/happyhouse/controller/HouseController.java)



###### [Controller - Data]

Data를 반환해야 하는 경우이다. 이때는 @ResponseBody를 추가해주어야 하며 JSON 형태로 데이터를 변환할 수 있다.



```java
@RestController
@RequestMapping("/entry")
public class EntryAPIController {

    public static final Logger logger = LoggerFactory.getLogger(EntryAPIController.class);

    @Autowired
    private EntryService entryService;

    @ApiOperation(value = "참여자의 상세 정보를 반환한다.", response = Entry.class)
    @GetMapping("/{entryNo}")
    public ResponseEntity<Entry> findEntryByNo(@PathVariable int entryNo) throws Exception {
        return new ResponseEntity<Entry>(
                entryService.findEntryByNo(entryNo), HttpStatus.OK
        );
    }

```

[코드 출처 : 나](https://github.com/oheong/Possible_Red/blob/master/backend/src/main/java/com/ssafy/SNS201/controller/EntryAPIController.java)

#### @RestController (Spring Restful Controller)

@Controller에 @ResponseBody가 추가된 것으로, JSON 형태로 객체 데이터를 반환하는 것이다.

Restful API를 개발할 때 주로 사용된다.




