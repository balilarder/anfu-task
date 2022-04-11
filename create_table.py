CREATE_POI_DATA_TABLE = """
USE [moi_avm]

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[poi_data](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[county] [varchar](50) NOT NULL,
	[data_catagory] [varchar](50) NOT NULL,
	[form_no] [varchar](50) NOT NULL,
	[t_station_min_distance_count] [int] NULL,
	[t_station_line_distance_count] [int] NULL,
	[t_station_min_distance_name] [varchar](200) NULL,
	[t_station_line_distance_name] [varchar](200) NULL,
	[t_station_min_distance] [decimal](18, 2) NULL,
	[t_station_line_distance] [decimal](18, 2) NULL,
	
	[junction_min_distance_count] [int] NULL,
	[junction_line_distance_count] [int] NULL,
	[junction_min_distance_name] [varchar](200) NULL,
	[junction_line_distance_name] [varchar](200) NULL,
	[junction_min_distance] [decimal](18, 2) NULL,
	[junction_line_distance] [decimal](18, 2) NULL,
	[school_min_distance_count] [int] NULL,
	[school_line_distance_count] [int] NULL,
	[school_min_distance_name] [varchar](200) NULL,
	[school_line_distance_name] [varchar](200) NULL,
	
	[school_min_distance] [decimal](18, 2) NULL,
	[school_line_distance] [decimal](18, 2) NULL,
	[service_facilities_min_distance_count] [int] NULL,
	[service_facilities_line_distance_count] [int] NULL,
	[service_facilities_min_distance_name] [varchar](200) NULL,
	[service_facilities_line_distance_name] [varchar](200) NULL,
	[service_facilities_min_distance] [decimal](18, 2) NULL,
	[service_facilities_line_distance] [decimal](18, 2) NULL,
	
	[market_min_distance_count] [int] NULL,
	[market_line_distance_count] [int] NULL,
	[market_min_distance_name] [varchar](200) NULL,
	[market_line_distance_name] [varchar](200) NULL,
	[market_min_distance] [decimal](18, 2) NULL,
	[market_line_distance] [decimal](18, 2) NULL,
	[park_min_distance_count] [int] NULL,
	[park_line_distance_count] [int] NULL,
	[park_min_distance_name] [varchar](200) NULL,
	[park_line_distance_name] [varchar](200) NULL,
	
	[park_min_distance] [decimal](18, 2) NULL,
	[park_line_distance] [decimal](18, 2) NULL,
	[station_min_distance_count] [int] NULL,
	[station_line_distance_count] [int] NULL,
	[station_min_distance_name] [varchar](200) NULL,
	[station_line_distance_name] [varchar](200) NULL,
	[station_min_distance] [decimal](18, 2) NULL,
	[station_line_distance] [decimal](18, 2) NULL,
	
	[parking_min_distance_count] [int] NULL,
	[parking_line_distance_count] [int] NULL,
	[parking_min_distance_name] [varchar](200) NULL,
	[parking_line_distance_name] [varchar](200) NULL,
	[parking_min_distance] [decimal](18, 2) NULL,
	[parking_line_distance] [decimal](18, 2) NULL,
	[bad_facilities_min_distance_count] [int] NULL,
	[bad_facilities_line_distance_count] [int] NULL,
	[bad_facilities_min_distance_name] [varchar](200) NULL,
	
	[bad_facilities_line_distance_name] [varchar](200) NULL,
	[bad_facilities_min_distance] [decimal](18, 2) NULL,
	[bad_facilities_line_distance] [decimal](18, 2) NULL,
	[created_at] [datetime] NOT NULL,
	[updated_at] [datetime] NULL
) ON [PRIMARY]

"""


CREATE_PARKING_ADJUST_TABLE = """
USE [moi_avm]
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON
CREATE TABLE [dbo].[parking_adjust](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[county] [varchar](20) NOT NULL,
	[region] [varchar](20) NOT NULL,
	[office_sec_no] [varchar](20) NOT NULL,
	[landno] [varchar](20) NOT NULL,
	[building_type] [varchar](30) NOT NULL,
	[car_type] [varchar](3) NOT NULL,
	[car_price_landno] [decimal](18, 0) NULL,
	[car_price_office_sec_no] [decimal](18, 0) NULL,
	[car_price_region] [decimal](18, 0) NULL,
	[car_price_county] [decimal](18, 0) NULL,
	[car_price_county_nontype] [decimal](18, 0) NULL,
	[car_area_m_landno] [decimal](18, 2) NULL,
	[car_area_m_office_sec_no] [decimal](18, 2) NULL,
	[car_area_m_region] [decimal](18, 2) NULL,
	[car_area_m_county] [decimal](18, 2) NULL,
	[car_area_m_county_nontype] [decimal](18, 2) NULL,
	[created_at] [datetime] NOT NULL,
	[updated_at] [datetime] NULL
) ON [PRIMARY]
"""

CREATE_MASTER_TABLE = """
USE [moi_avm]
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON
CREATE TABLE [dbo].[master](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[county] [varchar](50) NOT NULL,
	[form_no] [varchar](50) NOT NULL,
	[town] [varchar](50) NOT NULL,
	[trans_type] [varchar](100) NOT NULL,
	[raw_address] [varchar](512) NOT NULL,
	[land_area_m] [varchar](20) NULL,
	[land_total_area_m] [varchar](20) NULL,
	[urban_zone] [varchar](512) NULL,
	[urban_zone_new] [varchar](512) NULL,
	[non_urban_zone] [varchar](50) NULL,
	[non_urban_use] [varchar](50) NULL,
	[trans_date] [varchar](20) NULL,
	[trans_num] [varchar](50) NULL,
	[trans_land] [int] NULL,
	[trans_building] [int] NULL,
	[trans_car] [int] NULL,
	[trans_floor] [varchar](200) NULL,
	[total_floor] [varchar](200) NULL,
	[building_type] [varchar](50) NULL,
	[main_usage] [varchar](max) NULL,
	[material] [varchar](1024) NULL,
	[completion_date] [varchar](20) NULL,
	[building_total_area_m] [varchar](20) NULL,
	[main_building_area_m] [varchar](20) NULL,
	[ancillary_building_area_m] [varchar](20) NULL,
	[room] [varchar](20) NULL,
	[living_room] [varchar](20) NULL,
	[bath] [varchar](20) NULL,
	[building_compartment] [varchar](10) NULL,
	[management] [varchar](10) NULL,
	[total_price] [varchar](20) NULL,
	[unit_price] [varchar](20) NULL,
	[car_type] [varchar](max) NULL,
	[car_area_m] [varchar](20) NULL,
	[car_price] [varchar](20) NULL,
	[car_area_m_revise] [varchar](20) NULL,
	[car_price_revise] [varchar](20) NULL,
	[note] [varchar](max) NULL,
	[is_three_month] [varchar](50) NULL,
	[is_trans_all] [varchar](50) NULL,
	[age] [varchar](20) NULL,
	[ave_slope] [varchar](20) NULL,
	[road_width] [varchar](20) NULL,
	[land_shape] [varchar](50) NULL,
	[road_type] [varchar](50) NULL,
	[land_depth] [varchar](20) NULL,
	[land_width] [varchar](20) NULL,
	[twd97_x] [varchar](20) NULL,
	[twd97_y] [varchar](20) NULL,
	[is_include_1f] [varchar](50) NULL,
	[is_include_base] [varchar](50) NULL,
	[build_trans_floor] [varchar](20) NULL,
	[living_area] [varchar](1000) NULL,
	[land_trans_ratio] [varchar](20) NULL,
	[merge_land_cnt] [varchar](20) NULL,
	[complex_name] [varchar](300) NULL,
	[building_no] [nvarchar](200) NULL,
	[license_no] [nvarchar](200) NULL,
	[construction_rate] [varchar](20) NULL,
	[volume_rate] [varchar](20) NULL,
	[land_price_sec] [varchar](50) NULL,
	[is_land_merge] [varchar](50) NULL,
	[has_elevator] [varchar](10) NULL,
	[has_volume_calculator] [varchar](50) NULL,
	[has_price_calculator] [varchar](50) NULL,
	[expose_type] [varchar](50) NULL,
	[spec_trans_type] [varchar](200) NULL,
	[registration_date] [varchar](20) NULL,
	[urban_type] [varchar](50) NULL,
	[office_code] [varchar](20) NULL,
	[sec_no] [varchar](20) NULL,
	[land_no] [varchar](20) NULL,
	[geom] [geometry] NULL,
	[created_at] [datetime] NOT NULL,
	[updated_at] [datetime] NULL,
	[landno] [varchar](50) NULL,
	[car_cnt] [int] NULL,
	[town_village] [nvarchar](50) NULL,
 CONSTRAINT [PK_master] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
"""