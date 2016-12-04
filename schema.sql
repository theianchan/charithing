drop table if exists causes;
create table causes (
    id integer primary key autoincrement,
    name text not null,
    emoji text not null,
    why_care text not null,
    why_now text not null,
    more_info text not null,
    national_description text not null,
    local_description text not null,
    cause_id integer not null
)
