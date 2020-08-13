package www.example.com.restaurantdetails.frominternet.model.fetchrestaurants;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

public class RestaurantModel {

    @SerializedName("results_found")
    @Expose
    private String resultsFound;
    @SerializedName("results_start")
    @Expose
    private String resultsStart;
    @SerializedName("results_shown")
    @Expose
    private String resultsShown;
    @SerializedName("restaurants")
    @Expose
    private List<Restaurant> restaurants;

    public int getResultsFound() {
        return Integer.parseInt(resultsFound);
    }

    public void setResultsFound(String resultsFound) {
        this.resultsFound = resultsFound;
    }

    public int getResultsStart() {
        return Integer.parseInt(resultsStart);
    }

    public void setResultsStart(String resultsStart) {
        this.resultsStart = resultsStart;
    }

    public int getResultsShown() {
        return Integer.parseInt(resultsShown);
    }

    public void setResultsShown(String resultsShown) {
        this.resultsShown = resultsShown;
    }

    public List<Restaurant> getRestaurants() {
        return restaurants;
    }

    public void setRestaurants(List<Restaurant> restaurants) {
        this.restaurants = restaurants;
    }
}
