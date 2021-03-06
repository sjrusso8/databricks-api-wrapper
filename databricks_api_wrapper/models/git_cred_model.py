# generated by datamodel-codegen:
#   filename:  gitcredentials-2.0-azure.yaml
#   timestamp: 2022-05-14T13:19:23+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class CredentialId(BaseModel):
    __root__: int = Field(
        ...,
        description='ID of the credential object in the workspace.',
        example=93488329053511,
    )


class GitUsername(BaseModel):
    __root__: str = Field(
        ...,
        description='Git username. Note: If using azureDevOpsServicesAAD as your Git provider on Azure, you should omit this field and the personal_access_token field. When you authenticate to the [Repos API](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/repos), you must use an [Azure Active Directory token](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/).',
        example='testuser',
    )


class GitProvider(BaseModel):
    __root__: str = Field(
        ...,
        description='Git provider. This field is case-insensitive. The available Git providers are awsCodeCommit, azureDevOpsServices, azureDevOpsServicesAAD, bitbucketCloud, bitbucketServer, gitHub, gitHubEnterprise, gitLab, and gitLabEnterpriseEdition. When this field is set to azureDevOpsServicesAAD, we use [Azure Active Directory OAuth tokens](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow) instead of [Azure DevOps personal access tokens](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page) to authenticate Git requests to Azure DevOps.',
        example='gitHub',
    )


class PersonalAccessToken(BaseModel):
    __root__: str = Field(
        ...,
        description='The personal access token used to authenticate to the corresponding Git provider. Note: If using azureDevOpsServicesAAD as your Git provider on Azure, you should omit this field and the git_username field. When you authenticate to the [Repos API](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/repos), you must use an [Azure Active Directory token](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/).',
        example='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',
    )


class GetCredentialResponse(BaseModel):
    credential_id: Optional[CredentialId] = None
    git_username: Optional[GitUsername] = None
    git_provider: Optional[GitProvider] = None


class GetCredentialsResponse(BaseModel):
    credentials: Optional[List[GetCredentialResponse]] = None


class CreateCredentialRequest(BaseModel):
    personal_access_token: Optional[PersonalAccessToken] = None
    git_username: Optional[GitUsername] = None
    git_provider: GitProvider


class UpdateCredentialRequest(BaseModel):
    personal_access_token: Optional[PersonalAccessToken] = None
    git_username: Optional[GitUsername] = None
    git_provider: Optional[GitProvider] = None


class Error(BaseModel):
    error_code: Optional[str] = Field(None, description='Error code')
    message: Optional[str] = Field(
        None,
        description='Human-readable error message describing the cause of the error.',
    )
