create table if not exists youtuber_info (
    id serial primary key,  
    channel_id varchar(100) unique not null, 
    profile_image text,
    channel_url text,
    subscriber_count bigint,
    video_count integer,
    avg_video_duration_seconds integer,
    latest_video_uploaded_at timestamp,
    keywords text[],
    description text,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

insert into youtuber_info (
    channel_id,
    profile_image,
    channel_url,
    subscriber_count,
    video_count,
    avg_video_duration_seconds,
    latest_video_uploaded_at,
    keywords,
    description
)
values (
    'test_channel_001',
    'https://example.com/profile.jpg',
    'https://youtube.com/channel/test_channel_001',
    100000,
    120,
    900,
    now(),
    array['여행', '브이로그'],
    '여행 브이로그 채널'
);