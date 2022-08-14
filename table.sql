drop table if exists users;
create table users
(
    id       bigint(20) not null primary key auto_increment,
    username     varchar(16)    default null unique,
    password varchar(16)    default null,
    phone    varchar(16)    default null,
    email    varchar(32)    default null,
    sex      enum ('男','女') default '男',
    birthday date,
    state    int            default null
);

INSERT INTO mutex.users (id, username, password, phone, email, sex, birthday, state)
VALUES (1, 'Admin', '123456', '654321', '123@qq.com', '男', '1999-06-02', 0);
INSERT INTO mutex.users (id, username, password, phone, email, sex, birthday, state)
VALUES (2, 'hg', '654321', '123456', '456@qq.com', '男', '2022-08-09', 1);
