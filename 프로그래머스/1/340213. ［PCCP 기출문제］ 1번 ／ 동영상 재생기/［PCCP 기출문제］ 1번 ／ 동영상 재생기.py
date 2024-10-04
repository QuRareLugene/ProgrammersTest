def convert_second(time):
    input_minute = time.split(":")[0]
    input_second = time.split(":")[1]
    time_in_sec = int(input_minute) * 60 + int(input_second)
    return time_in_sec

def convert_timestamp(timestamp):
    output_minute = timestamp // 60
    output_second = timestamp % 60
    return f"{output_minute:0>2d}:{output_second:0>2d}"

def check_opening(current_sec, startpoint, endpoint):
    if (current_sec >= startpoint) and (current_sec <= endpoint):
        return True
    else:
        return False

def solution(video_len, pos, op_start, op_end, commands):
    
    total_length = convert_second(video_len)
    timestamp = convert_second(pos)
    start_dtm = convert_second(op_start)
    end_dtm = convert_second(op_end)
    
    if(check_opening(timestamp, start_dtm, end_dtm)):
        timestamp = end_dtm
    
    for item in commands:
        if(item == "next"):
            timestamp += 10
        elif(item == "prev"):
            timestamp -= 10
        if(timestamp > total_length):
            timestamp = total_length
        if(timestamp <=0):
            timestamp = 0
        if(check_opening(timestamp, start_dtm, end_dtm)):
            timestamp = end_dtm
    return convert_timestamp(timestamp)