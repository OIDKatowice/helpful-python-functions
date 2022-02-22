import numpy as np
import folium
from folium.plugins import geocoder
from folium.plugins import MeasureControl
from branca.element import Template, MacroElement
def interactive_choropleth(data, color_variable, tooltip_fields, tooltip_aliases, legend_title= "My Legend Title", map_location=[37.8, -96], map_zoom= 4, map_tiles= 'CartoDB positron', folium_layer_name= 'interactive choropleth', zoom_on_click= True, add_geocoder= True, add_measuring= True, download_html_path = None):
    m = folium.Map(location= map_location, zoom_start= map_zoom, tiles= map_tiles)

    # Set up Bins
    bins = np.linspace(data[color_variable].min(), data[color_variable].max(), 8)
    # Define Pallete for Choropleth
    choropleth_colors = np.array(['#fff7ec', '#fee8c8', '#fdd49e', '#fdbb84', '#fc8d59', '#ef6548', '#d7301f', '#990000'])
    
    # Polygon Style Function
    def style_function(feature):
        sal = feature['properties'][color_variable]
        return {'color':'black', 
                'fillOpacity': 0.8,
                'weight': 1,
                'fillColor':  
                '#d9d9d9' 
                    if (sal == np.nan or sal is None)
                    else choropleth_colors[0] if sal >= bins[0] and sal < bins[1]
                    else choropleth_colors[1] if sal >= bins[1] and sal < bins[2]
                    else choropleth_colors[2] if sal >= bins[2] and sal < bins[3]
                    else choropleth_colors[3] if sal >= bins[3] and sal < bins[4]
                    else choropleth_colors[4] if sal >= bins[4] and sal < bins[5]
                    else choropleth_colors[5] if sal >= bins[5] and sal < bins[6]
                    else choropleth_colors[6] if sal >= bins[6] and sal < bins[7]
                    else choropleth_colors[7] if sal >= bins[7]
                    else 'black'}

    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}

    folium.GeoJson(
        data = data,
        style_function=style_function,
        highlight_function=highlight_function,
        name= folium_layer_name,
        overlay=True,
        control=True,
        show=True,
        smooth_factor=None,
        zoom_on_click= zoom_on_click,
        tooltip= folium.features.GeoJsonTooltip(
            fields= tooltip_fields,
            aliases=tooltip_aliases,
            style = """
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 2px,
            box-shadow: 3px; 
            """)
    ).add_to(m)

    ####################################### Adding in Manual Legend #######################################

    template = """
    {% macro html(this, kwargs) %}

    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>jQuery UI Draggable - Default functionality</title>
      <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

      <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
      <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

      <script>
      $( function() {
        $( "#maplegend" ).draggable({
                        start: function (event, ui) {
                            $(this).css({
                                right: "auto",
                                top: "auto",
                                bottom: "auto"
                            });
                        }
                    });
    });

      </script>
    </head>
    <body>


    <div id='maplegend' class='maplegend' 
        style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
         border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>

    <div class='legend-title'>""" + legend_title + """</div>
    <div class='legend-scale'>
      <ul class='legend-labels', style="font-weight: bold;">
        <li><span style='background:#fff7ec;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
        <li><span style='background:#fee8c8;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
        <li><span style='background:#fdd49e;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
        <li><span style='background:#fdbb84;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(bins[4])) + """</li>
        <li><span style='background:#fc8d59;opacity:0.8;'></span>""" + str(round(bins[4])) + """ - """ + str(round(bins[5])) + """</li>
        <li><span style='background:#ef6548;opacity:0.8;'></span>""" + str(round(bins[5])) + """ - """ + str(round(bins[6])) + """</li>
        <li><span style='background:#d7301f;opacity:0.8;'></span>""" + str(round(bins[6])) + """ - """ + str(round(data[color_variable].max())) + """</li>

      </ul>
    </div>
    </div>

    </body>
    </html>

    <style type='text/css'>
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 1px solid #999;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}"""

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)
    
    if add_measuring == True:
        m.add_child(MeasureControl(position = 'bottomleft', primary_length_unit='miles', secondary_length_unit='meters', primary_area_unit='sqmiles', secondary_area_unit=np.nan))
    if add_geocoder == True:
        folium.plugins.Geocoder().add_to(m)
    if download_html_path is not None:
        m.save(f'{download_html_path}/interactive_choropleth.html')
    return m
