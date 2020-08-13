package www.example.com.restaurantdetails;

import www.example.com.restaurantdetails.frominternet.RestApi;
import www.example.com.restaurantdetails.frominternet.RestApiFactory;

public class Repository {

    private RestApi retrofitClient;

    public Repository(){
        retrofitClient = RestApiFactory.create();
    }

    public RestaurantDataFactory getRestaurantListFactory(int cityId) {
        return new RestaurantDataFactory(cityId);
    }
}
