# @RequestBody, @PathVariable 차이



##### @RequestBody

Http요청의 Body 부분을 Java 객체로 받을 수 있게 해주는 어노테이션이다.

주로 JSON을 받을 때 사용한다.

JSON에 데이터를 담아 컨트롤러로 넘겨주면 아주쉽게 값을 매핑할 수 있다.

파라미터가 고스란히 java객체에 담기기 때문이다.

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




