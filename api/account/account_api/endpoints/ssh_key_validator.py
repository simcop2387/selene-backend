# Mycroft Server - Backend
# Copyright (C) 2019 Mycroft AI Inc
# SPDX-License-Identifier: 	AGPL-3.0-or-later
#
# This file is part of the Mycroft Server.
#
# The Mycroft Server is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
"""Endpoint to validate the contents of the SSH public key."""

from http import HTTPStatus

from selene.api import SeleneEndpoint
from selene.util.ssh import validate_rsa_public_key


class SshKeyValidatorEndpoint(SeleneEndpoint):
    """Validate the contents of an SSH public key."""

    def get(self, ssh_key):
        """Handle and HTTP GET request."""
        self._authenticate()
        ssh_key_is_valid = validate_rsa_public_key(ssh_key)

        return dict(isValid=ssh_key_is_valid), HTTPStatus.OK