SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CW2].[TrailFeatures](
	[TrailID] [int] NOT NULL,
	[FeaturesID] [int] NOT NULL,
	CONSTRAINT PK_TrailFeatures PRIMARY KEY CLUSTERED ([TrailID], [FeaturesID]),
    CONSTRAINT FK_TrailFeatures_Trail FOREIGN KEY ([TrailID]) REFERENCES [CW2].[Trail] ([TrailID]),
    CONSTRAINT FK_TrailFeatures_Features FOREIGN KEY ([FeaturesID]) REFERENCES [CW2].[Features] ([FeaturesID])
) ON [PRIMARY]
GO
