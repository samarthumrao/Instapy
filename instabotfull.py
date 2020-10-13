
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'username'  
insta_password = 'password'

# starting instapy session
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4600,
                                    min_followers=100,
                                    min_following=50)

    session.set_dont_like(["pizza", "store", "food", "sad", "people", "paper"])

    # activity
    session.like_by_tags(['memesdaily', 'minecraft', 'memegod', 'csgo', 'games'], amount=3)
    session.set_do_comment(True, percentage=50)
    session.set_comments(['I love your post !! heheheh', 'wow', 'Cant stop laughing', 'amazing !!', 'best one ever', 'LOL'])
    session.set_do_follow(True, percentage=50)