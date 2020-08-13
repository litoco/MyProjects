package www.example.com.restaurantdetails.view;

import android.util.Log;

import androidx.annotation.NonNull;
import androidx.lifecycle.MutableLiveData;
import androidx.paging.ItemKeyedDataSource;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import www.example.com.restaurantdetails.frominternet.RestApi;
import www.example.com.restaurantdetails.frominternet.RestApiFactory;
import www.example.com.restaurantdetails.frominternet.model.fetchrestaurants.Restaurant;
import www.example.com.restaurantdetails.frominternet.model.fetchrestaurants.RestaurantModel;

public class RestaurantDataSource extends ItemKeyedDataSource<Integer, Restaurant> {

    private RestApi retrofitClient;
    private MutableLiveData<String> networkState;
    private MutableLiveData<String> initialLoading;
    private int cityId;
    private int size=0;

    public RestaurantDataSource(int cityId){
        this.retrofitClient = RestApiFactory.create();
        networkState = new MutableLiveData<>();
        initialLoading = new MutableLiveData<>();
        this.cityId = cityId;
    }

    @Override
    public void loadInitial(@NonNull LoadInitialParams<Integer> params, @NonNull LoadInitialCallback<Restaurant> callback) {
        initialLoading.postValue("loading");
        networkState.postValue("loading");
        retrofitClient.fetchRestaurants(cityId, "city", 0)
        .enqueue(new Callback<RestaurantModel>() {
            @Override
            public void onResponse(Call<RestaurantModel> call, Response<RestaurantModel> response) {
                if(response.isSuccessful() && response.body()!=null){
                    Log.e("RestaurantDataSource", "success "+ response.body().getRestaurants().get(0).toString());
                    callback.onResult(response.body().getRestaurants(), 0, 21);
                    initialLoading.postValue("loaded");
                    networkState.postValue("loaded");
                    size+=response.body().getRestaurants().size();
                }else{
                    Log.e("RestaurantDataSource", "some problem: "+response.message());
                    initialLoading.postValue("failed");
                    networkState.postValue("failed");
                }
            }

            @Override
            public void onFailure(Call<RestaurantModel> call, Throwable t) {
                Log.e("RestaurantDataSource", "problem: "+t.toString());
                initialLoading.postValue("failed");
                networkState.postValue("failed");
            }
        });
    }   

    @Override
    public void loadAfter(@NonNull LoadParams<Integer> params, @NonNull LoadCallback<Restaurant> callback) {
        networkState.postValue("loading");
        retrofitClient.fetchRestaurants(cityId, "city", size)
        .enqueue(new Callback<RestaurantModel>() {
            @Override
            public void onResponse(Call<RestaurantModel> call, Response<RestaurantModel> response) {
                if(response.isSuccessful() && response.body()!=null){
                    Log.e("RestaurantDataSource", "successes: "+ response.body().getResultsStart());
                    callback.onResult(response.body().getRestaurants());
                    networkState.postValue("loaded");
                    size+=response.body().getRestaurants().size();
                }else networkState.postValue("failed");
            }

            @Override
            public void onFailure(Call<RestaurantModel> call, Throwable t) {
                networkState.postValue("failed");
            }
        });
    }

    @Override
    public void loadBefore(@NonNull LoadParams<Integer> params, @NonNull LoadCallback<Restaurant> callback) {

    }

    @NonNull
    @Override
    public Integer getKey(@NonNull Restaurant item) {
        return null;
    }

    public MutableLiveData<String> getInitialLoading() {
        return initialLoading;
    }

    public MutableLiveData<String> getNetworkState() {
        return networkState;
    }
}
