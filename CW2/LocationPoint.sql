SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CW2].[LocationPoint](
	[LocationPoint] [int] NOT NULL,
	[Latitude] [decimal](9, 6) NOT NULL,
	[Longitude] [decimal](9, 6) NOT NULL,
	[Description] [varchar](200) NOT NULL
	CONSTRAINT PK_LocationPoint PRIMARY KEY CLUSTERED ([LocationPointID] ASC)
) ON [PRIMARY]
GO

