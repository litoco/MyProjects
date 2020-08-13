package www.example.com.restaurantdetails;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import androidx.paging.LivePagedListBuilder;
import androidx.paging.PagedList;

import www.example.com.restaurantdetails.frominternet.model.fetchrestaurants.Restaurant;
import www.example.com.restaurantdetails.frominternet.model.fetchrestaurants.RestaurantModel;

public class MainActivityViewModel extends ViewModel {

    private Repository repository;
    private LiveData<PagedList<Restaurant>> restaurantsDetailList;
    private MutableLiveData<String> networkState=new MutableLiveData<>();

    public MainActivityViewModel(){
        repository = new Repository();
    }

    public LiveData<PagedList<Restaurant>> getRestaurantsDetailList(int cityId) {
        if(restaurantsDetailList==null){
            RestaurantDataFactory factory = repository.getRestaurantListFactory(cityId);
            if(factory.getRestaurantModelMutableLiveData().getValue()!=null)
                networkState = factory.getRestaurantModelMutableLiveData().getValue().getNetworkState();

            PagedList.Config config = new PagedList.Config.Builder().setPageSize(20).setEnablePlaceholders(true).build();
            restaurantsDetailList = (new LivePagedListBuilder<>(factory, config)).build();
        }
        return restaurantsDetailList;
    }
}
