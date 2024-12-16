SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CW2].[Trail](
	[TrailID] [int] IDENTITY(1,1) NOT NULL,
	[TrailName] [varchar](50) NOT NULL,
	[TrailSummary] [varchar](500) NULL,
	[TrailDescription] [varchar](500) NULL,
	[Difficulty] [varchar](8)  NOT NULL CHECK ([Difficulty] IN ('Easy', 'Moderate', 'Hard', 'Very Hard')),
	[Location] [varchar](100) NOT NULL,
	[Length] [decimal](8, 2) NOT NULL,,
	[ElevationGain] [decimal](6, 2) NOT NULL,
	[RouteType] [varchar](25) NOT NULL,
	[OwnerID] [int] NOT NULL,
	CONSTRAINT PK_Trail PRIMARY KEY CLUSTERED ([TrailID] ASC),
    CONSTRAINT FK_Trail_User FOREIGN KEY ([OwnerID]) REFERENCES [CW2].[User] ([UserID])
) ON [PRIMARY]
GO

