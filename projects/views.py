import json
import os
import subprocess

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project, Hook


class HookReceiverView(APIView):
    def post(self, request, **kwargs):
        uuid = kwargs.get('uuid')
        project = get_object_or_404(Project, uuid=uuid)

        os.chdir(project.path)

        commands = project.commands.split("\n")
        commands_result = ""
        for command in commands:
            output = subprocess.check_output(command, shell=True)
            commands_result += str(output) + "\n"

        Hook.objects.create(
            project=project,
            body=json.dumps(request.data),
            commands_result=commands_result
        )

        return Response([commands_result])
