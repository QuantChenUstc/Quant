drop database if exists data_day;

create database data_day;

use data_day;

create table day(
    code char(11) not null,
    code_date DATE not null,
    display_name char(4) not null,
    abridge_name char(4) not null,
    open_price decimal(6,2) not null,
    close_price decimal(6,2) not null,
    high_price decimal(6,2) not null,
    low_price decimal(6,2) not null,
    pre_close decimal(6,2) not null,
    volume INT not null,
    allmoney INT not null,
    change_ratio decimal(4,2) not null,
    change_price decimal(6,2) not null,
    high_limit decimal(6,2) not null,
    low_limit decimal(6,2) not null,
    paused TINYINT not null,
    is_st TINYINT not null,
    volume_ratio decimal(6,2) not null,
    ma5 decimal(6,2) not null,
    ma10 decimal(6,2) not null,
    ma20 decimal(6,2) not null,
    ma30 decimal(6,2) not null,
    ma60 decimal(6,2) not null,
    ma180 decimal(6,2) not null,
    primary key(code, code_date)
);