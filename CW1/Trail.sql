SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CW1].[Trail](
	[TrailID] [int] IDENTITY(1,1) NOT NULL,
	[TrailName] [varchar](50) NOT NULL,
	[Length] [smallint] NOT NULL,
	[ElevationGain] [smallint] NOT NULL,
	[AverageCompletionTime] [varchar](10) NULL,
	[Rating] [decimal](3, 2) NULL,
	[RouteType] [varchar](25) NOT NULL,
	[Difficulty] [varchar](8) NOT NULL,
	[BestTimeToVisit] [varchar](25) NULL,
	[Location] [varchar](100) NOT NULL,
	[Description] [varchar](500) NULL
) ON [PRIMARY]
GO
ALTER TABLE [CW1].[Trail] ADD PRIMARY KEY CLUSTERED 
(
	[TrailID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([BestTimeToVisit]='December' OR [BestTimeToVisit]='November' OR [BestTimeToVisit]='October' OR [BestTimeToVisit]='September' OR [BestTimeToVisit]='August' OR [BestTimeToVisit]='July' OR [BestTimeToVisit]='June' OR [BestTimeToVisit]='May' OR [BestTimeToVisit]='April' OR [BestTimeToVisit]='March' OR [BestTimeToVisit]='February' OR [BestTimeToVisit]='January'))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([Difficulty]='Very Hard' OR [Difficulty]='Hard' OR [Difficulty]='Moderate' OR [Difficulty]='Easy'))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([ElevationGain]>=(0)))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([Length]>(0)))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([Location]=(upper(left([Location],(1)))+substring([Location],(2),len([Location])))))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([Rating]>=(0.00) AND [Rating]<=(5.00)))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([RouteType]=(upper(left([RouteType],(1)))+substring([RouteType],(2),len([RouteType])))))
GO
ALTER TABLE [CW1].[Trail]  WITH CHECK ADD CHECK  (([TrailName]=(upper(left([TrailName],(1)))+substring([TrailName],(2),len([TrailName])))))
GO
