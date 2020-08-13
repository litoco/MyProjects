package www.example.com.restaurantdetails.frominternet;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RestApiFactory {

    private static String BASE_URL = "https://developers.zomato.com/api/v2.1/";

    public static RestApi create(){
//        Gson gson = new GsonBuilder()
//                .setLenient()
//                .create();
        Retrofit retrofit = new Retrofit.Builder().baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        return retrofit.create(RestApi.class);
    }

}
