package www.example.com.restaurantdetails.view;

import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import androidx.paging.PagedList;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.textfield.TextInputLayout;

import java.util.Objects;

import www.example.com.restaurantdetails.MainActivityViewModel;
import www.example.com.restaurantdetails.R;
import www.example.com.restaurantdetails.RestaurantListAdapter;
import www.example.com.restaurantdetails.frominternet.model.fetchrestaurants.Restaurant;

public class SelectionFragment extends Fragment implements TextWatcher {

    private TextInputLayout city;
    private boolean isSearchClicked=false;
    private MainActivityViewModel mainActivityViewModel;
    private RecyclerView recyclerView;
    private RestaurantListAdapter listAdapter;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_selection, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        initViews(view);
        recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
        recyclerView.setAdapter(listAdapter);
        mainActivityViewModel.getRestaurantsDetailList(40).observe(getViewLifecycleOwner(), new Observer<PagedList<Restaurant>>() {
            @Override
            public void onChanged(PagedList<Restaurant> restaurantDetails) {
                listAdapter.submitList(restaurantDetails);
            }
        });
        Objects.requireNonNull(city.getEditText()).addTextChangedListener(this);
        city.setErrorIconDrawable(null);
        city.setEndIconOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(!city.getEditText().getText().toString().trim().equals("")) {
                    if (!isSearchClicked) {
                        isSearchClicked = true;
                        city.getEditText().clearFocus();
                        hideKeyboard(view);
                        /*here send a request to api to check city exists or not, then show all cities received as result in a list below search bar,
                         on click of any one of these list items move to next fragment and show list of restaurants based on the selection*/
                        new Handler().postDelayed(new Runnable() {
                            @Override
                            public void run() {
                                city.setError("Items are not delivered here");
                                city.setEndIconDrawable(requireContext().getResources().getDrawable(R.drawable.ic_cancel));
                            }
                        }, 5000);
                    } else {
                        isSearchClicked = false;
                        city.getEditText().setText("");
                        city.requestFocus();
                    }
                }else
                    Toast.makeText(requireContext(), "Empty city name not allowed", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void hideKeyboard(View view) {
        InputMethodManager imm = (InputMethodManager)requireContext().getSystemService(Context.INPUT_METHOD_SERVICE);
        if(imm!=null)
            imm.hideSoftInputFromWindow(view.getWindowToken(), 0);
    }

    private void initViews(View view) {
        mainActivityViewModel = new ViewModelProvider(requireActivity()).get(MainActivityViewModel.class);
        city = view.findViewById(R.id.selection_city);
        recyclerView = view.findViewById(R.id.selection_recycler_view);
        listAdapter = new RestaurantListAdapter(requireContext());
    }

    @Override
    public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) { }

    @Override
    public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
        if(charSequence.toString().trim().equals("")) {
            city.setEndIconDrawable(requireContext().getResources().getDrawable(R.drawable.ic_search));
            city.setError(null);
        }
    }

    @Override
    public void afterTextChanged(Editable editable) { }
}
