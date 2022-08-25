# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Gio Corp
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
    ScheduledExecutionResponse,
    ValidationResponse,
)
#from requests_oauthlib import OAuth1Session


class Netflix_as_a_serviceExtension(Extension):
    
    def execute_scheduled_processing(self, schedule):  # Scheduled process, not used
        self.logger.info(
            f"Received event for schedule  {schedule['id']}",
        )
        return ScheduledExecutionResponse.done()

    def approve_asset_request(self, request, template_id):
        self.logger.info(f'request_id={request["id"]} - template_id={template_id}')
        self.client.requests[request['id']]('approve').post(
            {
                'template_id': template_id,
            }
        )
        self.logger.warning(f"Approved request {request['id']}")

    def process_asset_purchase_request(self, request): # This function processes purchase subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_change_request(self, request): # This function processes change subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_cancel_request(self, request): # This function processes cancel subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_suspend_request(self, request): # This function processes suspend subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()
 
    def process_asset_resume_request(self, request): # This function processes resume subscription requests
        self.logger.info(
            f"Received event for request {request['id']}, type {request['type']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            f"in status {template_id}"
            self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()