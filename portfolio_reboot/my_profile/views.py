import json

# from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from .models import TreeNode


def treeNode(request):
    tree_node_id = request.GET.get('node_id')
    node = get_object_or_404(TreeNode, pk=tree_node_id)
    dict_obj = model_to_dict(node)
    return HttpResponse(json.dumps(dict_obj))
