import requests
import logging


class SitumAPI:
    api_email = 'gonzaloadrio@gmail.com'
    api_key = '0a0ac7b22d8ea2aa4c47d13df29d00fbec6c340dc745be82fe134dd1727c77f7'
    api_url = 'https://dashboard.situm.es/api/v1/'

    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    REQUEST_FAILED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    UNPROCESSABLE_ENTITY = 422
    SERVER_ERROR = 500
    INSUFICIENT_STORAGE = 507

    RESPONSE_CODES = {
        OK: 'Ok',
        BAD_REQUEST: 'Bad Request',
        UNAUTHORIZED: 'Unauthorized',
        REQUEST_FAILED: 'Request Failed',
        FORBIDDEN: 'Forbidden',
        NOT_FOUND: 'Not Found',
        UNPROCESSABLE_ENTITY: 'Unprocessable Entity',
        SERVER_ERROR: 'Server Error',
        INSUFICIENT_STORAGE: 'Insufficient Storage'
    }

    def __init__(self, api_email=api_email, api_key=api_key, api_url=api_url):
        self.api_email = api_email
        self.api_key = api_key
        self.api_url = api_url

    def get_buildings(self):
        headers = {'X-API-EMAIL': self.api_email, 'X-API-KEY': self.api_key}
        url = self.api_url + 'projects'
        res = requests.get(url=url, headers=headers)
        if res.status_code == self.OK:
            buildings = res.json()
            logging.info(buildings)
            return buildings
        else:
            logging.warning(self.RESPONSE_CODES[res.status_code])
            return None

    def get_building(self, building_id):
        headers = {'X-API-EMAIL': self.api_email, 'X-API-KEY': self.api_key}
        url = self.api_url + 'projects/{0}'.format(building_id)
        res = requests.get(url=url, headers=headers)
        if res.status_code == self.OK:
            building = res.json()
            logging.info(building)
            return building
        else:
            logging.warning(self.RESPONSE_CODES[res.status_code])
            return None

    def get_floors(self, building_id):
        headers = {'X-API-EMAIL': self.api_email, 'X-API-KEY': self.api_key}
        url = self.api_url + 'projects/{0}/floors'.format(building_id)
        res = requests.get(url=url, headers=headers)
        if res.status_code == self.OK:
            floors = res.json()
            logging.info(floors)
            return floors
        else:
            logging.warning(self.RESPONSE_CODES[res.status_code])
            return None

    def get_floor(self, floor_id):
        headers = {'X-API-EMAIL': self.api_email, 'X-API-KEY': self.api_key}
        url = self.api_url + 'floors/{0}'.format(floor_id)
        res = requests.get(url=url, headers=headers)
        if res.status_code == self.OK:
            floor = res.json()
            logging.info(floor)
            return floor
        else:
            logging.warning(self.RESPONSE_CODES[res.status_code])
            return None

    def get_analytics(self, building_id, date, date_end=None, device_id=None):
        headers = {'X-API-EMAIL': self.api_email, 'X-API-KEY': self.api_key}
        params = {'buiding_id': building_id, 'date': date}
        if date_end:
            params += {'date_end': date_end}
        if device_id:
            params += {'device_id': device_id}
        url = self.api_url + 'real_time/analytics/raw_pose_data'
        res = requests.get(url=url, headers=headers, params=params)
        if res.status_code == self.OK:
            floor = res.json()
            logging.info(floor)
            return floor
        else:
            logging.warning(self.RESPONSE_CODES[res.status_code])
            return None
