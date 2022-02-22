# Example Usage with CA County level teacher salary data
import geopandas as gpd
df = gpd.read_file("functions/folium/choropleth/county_df.json")
example = interactive_choropleth(
    data = df
    , color_variable = 'salary'
    , tooltip_fields = ['COUNTY_NAM', 'COUNTY_ABB', 'COUNTY_NUM', 'COUNTY_COD', 'salary_rank', 'salary']
    , tooltip_aliases = ['County Name', 'County Abbreviation', 'County Number', 'County Code', 'Salary Rank', 'Salary ($)']
    , legend_title= "CA School Salaries"
    , map_location=[37.411292, -118]
    , map_zoom= 4
    , map_tiles= 'CartoDB positron'
    , folium_layer_name= 'interactive choropleth'
    , zoom_on_click= True
    , add_geocoder= True
    , add_measuring= True
    , download_html_path = None
)
example 
