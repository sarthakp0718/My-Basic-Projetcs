import time

# Print current time as string
current_time = time.strftime('%H:%M:%S')
print("Full time (HH:MM:SS):", current_time)

# Print current hour
hour = time.strftime('%H')
print("Hour:", hour)

# Print current minute
minute = time.strftime('%M')
print("Minute:", minute)

# Print current second
second = time.strftime('%S')
print("Second:", second)
