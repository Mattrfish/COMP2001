SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CW2].[TrailLocationPt](
	[TrailID] [int] NOT NULL,
    [LocationPointID] [int] NOT NULL,
    [OrderNo] [int] NOT NULL,
    CONSTRAINT PK_TrailLocationPt PRIMARY KEY CLUSTERED ([TrailID], [LocationPointID]),
    CONSTRAINT FK_TrailLocationPt_Trail FOREIGN KEY ([TrailID]) REFERENCES [CW2].[Trail] ([TrailID]),
    CONSTRAINT FK_TrailLocationPt_LocationPoint FOREIGN KEY ([LocationPointID]) REFERENCES [CW2].[LocationPoint] ([LocationPointID])
) ON [PRIMARY]
GO

