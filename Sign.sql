Create table flights(
    id serial primary key,
    origin VARCHAR not null,
    destination varchar not null,
    duration integer not null
)