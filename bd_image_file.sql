CREATE TABLE `Image` (
  `image_id` INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name_file` VARCHAR(20) NOT NULL,
  `name_extension` VARCHAR(20) NOT NULL,
  `fecha` DATE NOT NULL
);

CREATE TABLE `Name_File` (
  `name_id` INTEGER NOT NULL AUTO_INCREMENT,
  `name_file` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`name_id`, `name_file`)
);

ALTER TABLE `Image` ADD FOREIGN KEY (`name_file`) REFERENCES `Name_File` (`name_file`);

CREATE UNIQUE INDEX `Image_index_0` ON `Image` (`image_id`);

CREATE UNIQUE INDEX `Name_File_index_1` ON `Name_File` (`name_id`);

CREATE UNIQUE INDEX `Name_File_index_2` ON `Name_File` (`name_file`);
