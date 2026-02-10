from data_day1 import temperatures

def mean(nums):
    if len(nums) == 0:
        return None
    total = 0.0
    for n in nums:
        total += n
    return total / len(nums)

def hottest_hour(nums):
    if len(nums) == 0:
        return (None, None)
    max_val = nums[0]
    max_idx = 0
    for idx in range(1, len(nums)):
        if nums[idx] > max_val:
            max_val = nums[idx]
            max_idx = idx
    return (max_val, max_idx)

def count_alerts(nums, threshold):
    count = 0
    for t in nums:
        if t >= threshold:
            count += 1
    return count

def make_report_line(day_label, nums, threshold):
    avg = mean(nums)
    mx, h = hottest_hour(nums)
    alerts = count_alerts(nums, threshold)
    return f"{day_label} | avg={avg:.1f}°C | max={mx:.1f}°C at h={h} | alerts(>={threshold})={alerts}"

if __name__ == "__main__":
    print("Run the exercise.")
