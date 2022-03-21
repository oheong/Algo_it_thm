# @RequestBody, @PathVariable, @RequestParam



##### @RequestBody

Http요청의 Body 부분을 Java 객체로 받을 수 있게 해주는 어노테이션이다.

주로 JSON을 받을 때 사용하며 원하는 타입의 객체로 반환해야 하는 경우에 사용한다.

JSON에 데이터를 담아 컨트롤러로 넘겨주면 아주쉽게 값을 매핑할 수 있다.

파라미터가 고스란히 java객체에 담기기 때문이다.

주로 비동기 처리 구현 시 @ResponseBody와 함께 자주 사용된다.


```java
@RestController
@RequestMapping("/booking/log")
public class BookingLogController {

    private static final Logger logger = LoggerFactory.getLogger(BookingLogController.class);

    private final BookingLogService logService;

    @PostMapping(value = "/addLog", consumes = "application/json", produces = "application/json")
    public int insertBookingLog(@RequestBody BookingLog bookingLog){
        logger.info("===== insert Booking Log =====");
        return logService.insertBookingLog(bookingLog);
    }

}
```

[코드 출처 : 나](https://github.com/oheong/uplus_intern_project/blob/main/BookingIF/src/main/java/com/uplus/bookingif/controller/BookingLogController.java)



##### @PathVariable

이 어노테이션으로 깔끔한 URI를 만들 수 있다.

URI 경로의 일부를 파라미터로 사용할 때 이용한다. (URI 경로에서 값을 가져온다)

> http://localhost:8003/concert/1



```java
@RestController
@RequestMapping("/concert")
public class ConcertController {
    private static final Logger logger = LoggerFactory.getLogger(ConcertController.class);

    private final ConcertService service;

    @GetMapping("/{concertId}")
    public Concert selectByConcertId(@PathVariable String concertId){
        logger.info("===== select Concert by concertId =====");
        return service.selectByConcertId(concertId);
    }

}
```

[코드 출처 : 나](https://github.com/oheong/uplus_intern_project/blob/main/ConcertIF/src/main/java/com/uplus/concertif/controller/ConcertController.java)



##### @RequestParam

쿼리 스트링에서 값을 가지고 온다.

@RequestParam에 명시된 매개변수 값은 반드시 파라미터로 값이 넘어와야 한다.

아닐 경우 400에러(Bad Request)발생.



