from django.db import models


class TreeNode(models.Model):
    title = models.CharField(max_length=100)
    left_text = models.CharField(max_length=100)
    left_child = models.ForeignKey("self", related_name="node_left_child", blank=True, null=True)
    right_text = models.CharField(max_length=100)
    right_child = models.ForeignKey("self", related_name="node_right_child", blank=True, null=True)
    top_text = models.CharField(max_length=500)
