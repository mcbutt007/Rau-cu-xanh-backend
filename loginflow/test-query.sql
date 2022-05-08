/* User table */
INSERT INTO USER (USERNAME,EMAIL,PASSWORD)
VALUES ( 'Paul', 'example@gmail.com', '123456' );

/* forget password email table */
INSERT INTO FORGET_PASSWORD_EMAIL (EMAIL, TIME_SENT)
VALUES ( 'example@gmail.com', CURRENT_TIMESTAMP );
