CREATE TABLE [tbl_user] (
  [id] integer PRIMARY KEY,
  [username] nvarchar(255) NOT NULL,
  [password] nvarchar(255) NOT NULL,
  [password_hint] nvarchar(255) NOT NULL,
  [master_password] nvarchar(255) NOT NULL,
  [profile_photo] blob,
  [created_at] timestamp,
  [pin] nvarchar(255) NOT NULL,
  [state] bool NOT NULL
)
GO

CREATE TABLE [tbl_categorie] (
  [id] integer PRIMARY KEY,
  [name] nvarchar(255) NOT NULL,
  [icon] blob,
  [user_id] integer NOT NULL,
  [created_at] timestamp,
  [state] bool NOT NULL
)
GO

CREATE TABLE [tbl_folder] (
  [id] integer PRIMARY KEY,
  [name] nvarchar(255) NOT NULL,
  [folder_color] nvarchar(255),
  [user_id] integer NOT NULL,
  [created_at] timestamp,
  [state] bool NOT NULL
)
GO

CREATE TABLE [tbl_password] (
  [id] integer PRIMARY KEY,
  [website] nvarchar(255) NOT NULL,
  [username_or_email] nvarchar(255) NOT NULL,
  [password] nvarchar(255) NOT NULL,
  [icon] blob,
  [category_id] integer,
  [folder_id] integer,
  [user_id] integer NOT NULL,
  [created_at] timestamp,
  [state] bool NOT NULL
)
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'Users data table',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'tbl_user';
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'Table allowing to set a category for passwords',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'tbl_categorie';
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'Table to organize passwords by folder',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'tbl_folder';
GO

EXEC sp_addextendedproperty
@name = N'Table_Description',
@value = 'Table to organize passwords by folder',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'tbl_password';
GO

ALTER TABLE [tbl_categorie] ADD FOREIGN KEY ([user_id]) REFERENCES [tbl_user] ([id])
GO

ALTER TABLE [tbl_folder] ADD FOREIGN KEY ([user_id]) REFERENCES [tbl_user] ([id])
GO

ALTER TABLE [tbl_password] ADD FOREIGN KEY ([user_id]) REFERENCES [tbl_user] ([id])
GO

ALTER TABLE [tbl_password] ADD FOREIGN KEY ([category_id]) REFERENCES [tbl_categorie] ([id])
GO

ALTER TABLE [tbl_password] ADD FOREIGN KEY ([folder_id]) REFERENCES [tbl_folder] ([id])
GO
