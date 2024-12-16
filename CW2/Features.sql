SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- Features Table
CREATE TABLE [CW2].[Features] (
    [FeaturesID] [int] IDENTITY(1,1) NOT NULL,
    [Feature] [varchar](20) NOT NULL,
    CONSTRAINT PK_Features PRIMARY KEY CLUSTERED ([FeaturesID] ASC)
) ON [PRIMARY];
GO