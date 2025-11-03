# 通过可公开调用的Github的API来访问我的公开信息。
import requests
def main(username):
    url = f"https://api.github.com/users/{username}/events"

    res = requests.get(
        url=url,
        verify=False
    )

    print(res.text)

if __name__ == "__main__":
    username = "therenobod"
    new_username = input("Your username:").split()
    if new_username:
        username = new_username
    print(username)
    main(username=username)
