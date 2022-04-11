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