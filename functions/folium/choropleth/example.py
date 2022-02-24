##### TESTING #####
# Example Usage with state population data
import geopandas as gpd
from . import interactive_choropleth
df = gpd.read_file("~/helpful-python-functions/functions/folium/choropleth/county_df.json")
example = interactive_choropleth(
    data = df
    , color_variable = 'salary'
    , pallette=Oranges_9
    , tooltip_fields = ['COUNTY_NAM', 'COUNTY_ABB', 'COUNTY_NUM', 'COUNTY_COD', 'salary_rank', 'salary']
    , tooltip_aliases = ['County Name', 'County Abbreviation', 'County Number', 'County Code', 'Salary Rank', 'Salary ($)']
    , legend_title= "CA School Salaries"
    , map_location=[37.411292, -118]
    , map_zoom= 6
    , map_tiles= 'CartoDB positron'
    , folium_layer_name= 'interactive choropleth'
    , zoom_on_click= True
    , add_geocoder= True
    , add_measuring= True
    , download_html_path = None
)
example