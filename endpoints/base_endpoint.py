class BaseEndpoint:
    response = None
    status_code = None
    response_json = None

    def check_response_is_200(self):
        assert self.status_code == 200

    def check_response_is_404(self):
        assert self.status_code == 404
