from notion_client import Client


class NotionDataInserter:
    def __init__(self, notion_token, database_id, page_id):
        self.notion_token = notion_token
        self.database_id = database_id
        self.page_id = page_id

        self.client = Client(auth=self.notion_token)

    def db_insert(self, title, genres, platform, ownership, price, cover_url):
        self.client.pages.create(
            **{
                "parent": {"database_id": self.database_id},
                "cover": {"external": {"url": cover_url}},
                "properties": {
                    "Title": {"title": [{"text": {"content": title}}]},
                    "Genre": {"multi_select": genres},
                    "Platform": {"select": {"name": platform}},
                    "Ownership": {"select": {"name": ownership}},
                    "Price": {"number": price},
                }
            }
        )
