from typing import Any, Dict, List, Optional, Union

import requests

from ...client import Client
from ...models.software_build import SoftwareBuild
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "exclude_fields": List[str],
    "include_fields": List[str],
}


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/builds/{uuid}".format(
        client.base_url,
        uuid=uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_exclude_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_fields, Unset):
        if exclude_fields is None:
            json_exclude_fields = None
        else:
            json_exclude_fields = exclude_fields

    json_include_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_fields, Unset):
        if include_fields is None:
            json_include_fields = None
        else:
            json_include_fields = include_fields

    params: Dict[str, Any] = {
        "exclude_fields": json_exclude_fields,
        "include_fields": json_include_fields,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: requests.Response) -> Optional[SoftwareBuild]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: SoftwareBuild
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = SoftwareBuild.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: requests.Response) -> Response[SoftwareBuild]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Client,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
) -> Response[SoftwareBuild]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    uuid: str,
    *,
    client: Client,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
) -> Optional[SoftwareBuild]:
    """View for api/v1/builds"""

    return sync_detailed(
        uuid=uuid,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
    ).parsed


async def async_detailed(
    uuid: str,
    *,
    client: Client,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
) -> Response[SoftwareBuild]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        exclude_fields=exclude_fields,
        include_fields=include_fields,
    )

    async with client.get_async_session().get(
        verify_ssl=client.verify_ssl, raise_for_status=True, **kwargs
    ) as response:
        content = await response.read()
        resp = requests.Response()
        resp.status_code = response.status
        resp._content = content

    return _build_response(response=resp)


async def async_(
    uuid: str,
    *,
    client: Client,
    exclude_fields: Union[Unset, None, List[str]] = UNSET,
    include_fields: Union[Unset, None, List[str]] = UNSET,
) -> Optional[SoftwareBuild]:
    """View for api/v1/builds"""

    return (
        await async_detailed(
            uuid=uuid,
            client=client,
            exclude_fields=exclude_fields,
            include_fields=include_fields,
        )
    ).parsed
