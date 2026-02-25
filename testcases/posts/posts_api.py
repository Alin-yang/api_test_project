from common.base_api import BaseApi

class PostsApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.module_url = "/posts"

    def get_post_list(self):
        """获取帖子列表"""
        return self.get(self.module_url)

    def get_post_detail(self, post_id):
        """获取帖子详情"""
        return self.get(f"{self.module_url}/{post_id}")

    def create_post(self, post_data):
        """创建新帖子"""
        return self.post(self.module_url, json=post_data)

    def update_post(self, post_id, update_data):
        """更新帖子"""
        return self.put(f"{self.module_url}/{post_id}", json=update_data)

    def delete_post(self, post_id):
        """删除帖子"""
        return self.delete(f"{self.module_url}/{post_id}")