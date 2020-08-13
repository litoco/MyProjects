package www.example.com.restaurantdetails;

import androidx.annotation.NonNull;
import androidx.lifecycle.MutableLiveData;
import androidx.paging.DataSource;

import www.example.com.restaurantdetails.view.RestaurantDataSource;

public class RestaurantDataFactory extends DataSource.Factory {

    private MutableLiveData<RestaurantDataSource> restaurantModelMutableLiveData;
    private int cityId;

    public RestaurantDataFactory(int cityId){
        restaurantModelMutableLiveData = new MutableLiveData<>();
        this.cityId = cityId;
    }

    @NonNull
    @Override
    public DataSource create() {
        RestaurantDataSource restaurantDataSource = new RestaurantDataSource(cityId);
        restaurantModelMutableLiveData.postValue(restaurantDataSource);
        return restaurantDataSource;
    }

    public MutableLiveData<RestaurantDataSource> getRestaurantModelMutableLiveData() {
        return restaurantModelMutableLiveData;
    }
}
