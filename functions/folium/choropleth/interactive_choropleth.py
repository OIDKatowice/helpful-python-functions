def interactive_choropleth(data, color_variable, tooltip_fields, tooltip_aliases, pallette= Oranges_8, legend_title= "My Legend Title", map_location=[37.8, -96], map_zoom= 4, map_tiles= 'CartoDB positron', folium_layer_name= 'interactive choropleth', zoom_on_click= True, add_geocoder= True, add_measuring= True, download_html_path = None):
    # Imports
    import numpy as np
    import folium
    from folium import plugins
    from folium.plugins import geocoder
    from folium.plugins import MeasureControl
    from branca.element import Template, MacroElement
    from palettable.colorbrewer.sequential import Blues_3,Blues_4,Blues_5,Blues_6,Blues_7,Blues_8,Blues_9,BuGn_3,BuGn_4,BuGn_5,BuGn_6,BuGn_7,BuGn_8,BuGn_9,BuPu_3,BuPu_4,BuPu_5,BuPu_6,BuPu_7,BuPu_8,BuPu_9,GnBu_3,GnBu_4,GnBu_5,GnBu_6,GnBu_7,GnBu_8,GnBu_9,Greens_3,Greens_4,Greens_5,Greens_6,Greens_7,Greens_8,Greens_9,Greys_3,Greys_4,Greys_5,Greys_6,Greys_7,Greys_8,Greys_9,OrRd_3,OrRd_4,OrRd_5,OrRd_6,OrRd_7,OrRd_8,OrRd_9,Oranges_3,Oranges_4,Oranges_5,Oranges_6,Oranges_7,Oranges_8,Oranges_9,PuBu_3,PuBu_4,PuBu_5,PuBu_6,PuBu_7,PuBu_8,PuBu_9,PuBuGn_3,PuBuGn_4,PuBuGn_5,PuBuGn_6,PuBuGn_7,PuBuGn_8,PuBuGn_9,PuRd_3,PuRd_4,PuRd_5,PuRd_6,PuRd_7,PuRd_8,PuRd_9,Purples_3,Purples_4,Purples_5,Purples_6,Purples_7,Purples_8,Purples_9,RdPu_3,RdPu_4,RdPu_5,RdPu_6,RdPu_7,RdPu_8,RdPu_9,Reds_3,Reds_4,Reds_5,Reds_6,Reds_7,Reds_8,Reds_9,YlGn_3,YlGn_4,YlGn_5,YlGn_6,YlGn_7,YlGn_8,YlGn_9,YlGnBu_3,YlGnBu_4,YlGnBu_5,YlGnBu_6,YlGnBu_7,YlGnBu_8,YlGnBu_9,YlOrBr_3,YlOrBr_4,YlOrBr_5,YlOrBr_6,YlOrBr_7,YlOrBr_8,YlOrBr_9,YlOrRd_3,YlOrRd_4,YlOrRd_5,YlOrRd_6,YlOrRd_7,YlOrRd_8,YlOrRd_9
    from palettable.colorbrewer.diverging import BrBG_3,BrBG_4,BrBG_5,BrBG_6,BrBG_7,BrBG_8,BrBG_9,BrBG_10,BrBG_11,PRGn_3,PRGn_4,PRGn_5,PRGn_6,PRGn_7,PRGn_8,PRGn_9,PRGn_10,PRGn_11,PiYG_3,PiYG_4,PiYG_5,PiYG_6,PiYG_7,PiYG_8,PiYG_9,PiYG_10,PiYG_11,PuOr_3,PuOr_4,PuOr_5,PuOr_6,PuOr_7,PuOr_8,PuOr_9,PuOr_10,PuOr_11,RdBu_3,RdBu_4,RdBu_5,RdBu_6,RdBu_7,RdBu_8,RdBu_9,RdBu_10,RdBu_11,RdGy_3,RdGy_4,RdGy_5,RdGy_6,RdGy_7,RdGy_8,RdGy_9,RdGy_10,RdGy_11,RdYlBu_3,RdYlBu_4,RdYlBu_5,RdYlBu_6,RdYlBu_7,RdYlBu_8,RdYlBu_9,RdYlBu_10,RdYlBu_11,RdYlGn_3,RdYlGn_4,RdYlGn_5,RdYlGn_6,RdYlGn_7,RdYlGn_8,RdYlGn_9,RdYlGn_10,RdYlGn_11,Spectral_3,Spectral_4,Spectral_5,Spectral_6,Spectral_7,Spectral_8,Spectral_9,Spectral_10,Spectral_11

    m = folium.Map(location= map_location, zoom_start= map_zoom, tiles= map_tiles)
    # Define Pallete for Choropleth
    choropleth_colors = pallette.hex_colors
    # Set up Bins
    bins = np.linspace(data[color_variable].min(), data[color_variable].max(), len(pallette.hex_colors))
    # Polygon Style Function
    def style_function(feature):
        sal = feature['properties'][color_variable]
        if len(pallette.hex_colors) < 3:
            raise ValueError("List of color strings must be of length 3 or greater")
        if len(pallette.hex_colors) > 9:
            raise ValueError("List of color strings must be of length 9 or less")
        elif len(pallette.hex_colors) == 3:
            return {'color':'black', 
                    'fillOpacity': 0.8,
                    'weight': 1,
                    'fillColor':   
                    '#d9d9d9'
                        if (sal == np.nan or sal is None)
                        else choropleth_colors[0] if sal >= bins[0] and sal < bins[1]
                        else choropleth_colors[1] if sal >= bins[1] and sal < bins[2]
                        else choropleth_colors[2] if sal >= bins[2]
                        else 'black'
                   }
        elif len(pallette.hex_colors) == 4:
            return {'color':'black', 
                    'fillOpacity': 0.8,
                    'weight': 1,
                    'fillColor':   
                    '#d9d9d9'
                        if (sal == np.nan or sal is None)
                        else choropleth_colors[0] if sal >= bins[0] and sal < bins[1]
                        else choropleth_colors[1] if sal >= bins[1] and sal < bins[2]
                        else choropleth_colors[2] if sal >= bins[2] and sal < bins[3]
                        else choropleth_colors[3] if sal >= bins[3]
                        else 'black'
                   }
        elif len(pallette.hex_colors) == 5:
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
                        else choropleth_colors[4] if sal >= bins[4]
                        else 'black'
                   }
        elif len(pallette.hex_colors) == 6:
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
                        else choropleth_colors[5] if sal >= bins[5]
                        else 'black'
                   }
        elif len(pallette.hex_colors) == 7:
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
                        else choropleth_colors[6] if sal >= bins[6]
                        else 'black'
                   }
        elif len(pallette.hex_colors) == 8:
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
                        else 'black'
                   }
        
        elif len(pallette.hex_colors) == 9:
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
                        else choropleth_colors[7] if sal >= bins[7] and sal < bins[8]
                        else choropleth_colors[8] if sal >= bins[8]
                        else 'black'
               }
        
    if len(pallette.hex_colors) < 3:
            raise ValueError("List of color strings must be of length 3 or greater")
    if len(pallette.hex_colors) > 9:
        raise ValueError("List of color strings must be of length 9 or less")
    elif len(pallette.hex_colors) == 3:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(data[color_variable].max())) + """</li>
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
            {% endmacro %}
            """
    elif len(pallette.hex_colors) == 4:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[3]) + """;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(data[color_variable].max())) + """</li>

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
            {% endmacro %}
            """
    elif len(pallette.hex_colors) == 5:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[3]) + """;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(bins[4])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[4]) + """;opacity:0.8;'></span>""" + str(round(bins[4])) + """ - """ + str(round(data[color_variable].max())) + """</li>

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
            {% endmacro %}
            """
    elif len(pallette.hex_colors) == 6:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[3]) + """;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(bins[4])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[4]) + """;opacity:0.8;'></span>""" + str(round(bins[4])) + """ - """ + str(round(bins[5])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[5]) + """;opacity:0.8;'></span>""" + str(round(bins[5])) + """ - """ + str(round(data[color_variable].max())) + """</li>

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
            {% endmacro %}
            """
    elif len(pallette.hex_colors) == 7:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[3]) + """;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(bins[4])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[4]) + """;opacity:0.8;'></span>""" + str(round(bins[4])) + """ - """ + str(round(bins[5])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[5]) + """;opacity:0.8;'></span>""" + str(round(bins[5])) + """ - """ + str(round(bins[6])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[6]) + """;opacity:0.8;'></span>""" + str(round(bins[6])) + """ - """ + str(round(data[color_variable].max())) + """</li>

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
            {% endmacro %}
            """
    elif len(pallette.hex_colors) == 8:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[3]) + """;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(bins[4])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[4]) + """;opacity:0.8;'></span>""" + str(round(bins[4])) + """ - """ + str(round(bins[5])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[5]) + """;opacity:0.8;'></span>""" + str(round(bins[5])) + """ - """ + str(round(bins[6])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[6]) + """;opacity:0.8;'></span>""" + str(round(bins[6])) + """ - """ + str(round(bins[7])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[7]) + """;opacity:0.8;'></span>""" + str(round(bins[7])) + """ - """ + str(round(data[color_variable].max())) + """</li>

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
            {% endmacro %}
            """
    elif len(pallette.hex_colors) == 9:
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
                <li><span style='background:""" + str(choropleth_colors[0]) + """;opacity:0.8;'></span>""" + str(round(bins[0])) + """ - """ + str(round(bins[1])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[1]) + """;opacity:0.8;'></span>""" + str(round(bins[1])) + """ - """ + str(round(bins[2])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[2]) + """;opacity:0.8;'></span>""" + str(round(bins[2])) + """ - """ + str(round(bins[3])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[3]) + """;opacity:0.8;'></span>""" + str(round(bins[3])) + """ - """ + str(round(bins[4])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[4]) + """;opacity:0.8;'></span>""" + str(round(bins[4])) + """ - """ + str(round(bins[5])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[5]) + """;opacity:0.8;'></span>""" + str(round(bins[5])) + """ - """ + str(round(bins[6])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[6]) + """;opacity:0.8;'></span>""" + str(round(bins[6])) + """ - """ + str(round(bins[7])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[7]) + """;opacity:0.8;'></span>""" + str(round(bins[7])) + """ - """ + str(round(bins[8])) + """</li>
                <li><span style='background:""" + str(choropleth_colors[8]) + """;opacity:0.8;'></span>""" + str(round(bins[8])) + """ - """ + str(round(data[color_variable].max())) + """</li>

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
            {% endmacro %}
            """
    
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
    
    macro = MacroElement()
    macro._template = Template(template)
    m.get_root().add_child(macro)
    if add_measuring == True:
        m.add_child(MeasureControl(position = 'bottomleft', primary_length_unit='miles', secondary_length_unit='meters', primary_area_unit='sqmiles', secondary_area_unit=np.nan))
    if add_geocoder == True:
        folium.plugins.Geocoder().add_to(m)
    folium.LayerControl().add_to(m)
    
    if download_html_path is not None:
        m.save(f'{download_html_path}/interactive_choropleth.html')
    return m

