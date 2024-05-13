import io
import os
import sys

from gtfs_functions import Feed
from gtfs_functions.gtfs_plots import map_gdf

gtfs_path = 'ct_gtfs.zip'
'''
Feed(gtfs_path: str, 
     time_windows: list = [0, 6, 9, 15, 19, 22, 24], 
     busiest_date: bool = True, 
     geo: bool = True, 
     patterns: bool = True, 
     start_date: str = None, 
     end_date: str = None)

 |  get_agency(self)
 |  get_avg_speeds(self): Calculate the average speed per route, segment and window.
 |  get_bbox(self)
 |  get_busiest_service_id(self): Returns the service_id with most trips as a string.
 |  get_calendar(self)
 |  get_calendar_dates(self)
 |  get_dates(self)
 |  get_dates_service_id(self)
 |  get_distance_between_stops(self)
 |      Compared H3 hex bins to DBSCAN clusters in this map:
 |      https://studio.foursquare.com/public/8436b10c-4ccc-48a3-a232-e8026f81a117
 |
 |      From what I see, the optimal resolution for our purposes is resolution=9.
 |      Taking the Hex bin at this resolution and its neighbors works as a better
 |      clustering method than DBSCAN.
 |      We can then only calculate the distance between each stop and the ones that
 |      are in the neighboring hex bins.
 |
 |  get_files(self)
 |  get_lines_freq(self)
 |      Calculates the frequency for each pattern of a route.
 |      Returns the bus frequency in minutes/bus broken down by
 |      time window.
 |  get_routes(self)
 |  get_routes_patterns(self, trips)
 |      Compute the different patterns of each route.
 |      returns (trips_patterns, routes_patterns)
 |  get_segments(self)
 |      Splits each route's shape into stop-stop LineString called segments
 |      Returns the segment geometry as well as additional segment information
 |  get_segments_freq(self)
 |  get_shapes(self)
 |  get_speeds(self)
 |  get_stop_times(self)
 |  get_stops(self)
 |  get_stops_freq(self)
 |      Get the stop frequencies. For each stop of each route it
 |      returns the bus frequency in minutes/bus broken down by
 |      time window.
 |  get_trips(self)
 |  parse_calendar(self)
'''
feed = Feed(gtfs_path)

routes = feed.routes
print("Routes")
print(routes)
print(routes.head(5))

stops = feed.stops
print("Stops")
print(stops.head(2))

stop_times = feed.stop_times
print("Stop Times")
print(stop_times.head(2))

trips = feed.trips
print("Trips")
print(trips.head(2))

shapes = feed.shapes
print("Shapes")
print(shapes.head(2))

time_windows = [0, 6, 9, 15.5, 19, 22, 24]

feed = Feed(gtfs_path, time_windows=time_windows)
stop_freq = feed.stops_freq
print("Stop Frequencies")
print(stop_freq.head(2))

#line_freq = feed.lines_freq
#print("Line Frequencies")
#line_freq.head()

# In CT data, direction_id is either 0 or 1
condition_dir = stop_freq.dir_id == '0'
condition_window = stop_freq.window == '6:00-9:00'

gdf = stop_freq.loc[(condition_dir & condition_window),:].reset_index()

#map_gdf(
#  gdf = gdf, 
#  variable = 'ntrips', 
#  colors = ["#d13870", "#e895b3" ,'#55d992', '#3ab071', '#0e8955','#066a40'], 
#  tooltip_var = ['min_per_trip'] , 
#  tooltip_labels = ['Frequency: '], 
#  breaks = [10, 20, 30, 40, 120, 200]
#)