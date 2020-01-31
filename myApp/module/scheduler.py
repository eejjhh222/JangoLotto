from apscheduler.schedulers.blocking import BlockingScheduler


def say_hi():
    print('hi')


sched = BlockingScheduler()
sched.add_job(say_hi, 'interval',seconds=5)
# sched.start()
# sched.pause()