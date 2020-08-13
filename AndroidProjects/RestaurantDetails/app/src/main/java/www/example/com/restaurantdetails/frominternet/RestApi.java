package www.example.com.restaurantdetails.frominternet;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Headers;
import retrofit2.http.Query;
import www.example.com.restaurantdetails.frominternet.model.fetchcities.CityModel;
import www.example.com.restaurantdetails.frominternet.model.fetchrestaurants.RestaurantModel;

public interface RestApi {

    @Headers("user-key: 5a59439663b8ce4ed5d46214021e17dc")
    @GET("cities")
    Call<CityModel> fetchCities(@Query("q") String cityName);

    @Headers("user-key: 5a59439663b8ce4ed5d46214021e17dc")
    @GET("search")
    Call<RestaurantModel> fetchRestaurants(@Query("entity_id") int cityId, @Query("entity_type") String entityTypeCityOrLandMark, @Query("start") int startingPosition);
}
