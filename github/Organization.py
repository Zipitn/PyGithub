############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Sebastien Besson <seb.besson@gmail.com>                       #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Matthew Neal <meneal@matthews-mbp.raleigh.ibm.com>            #
# Copyright 2016 Michael Pereira <pereira.m@gmail.com>                         #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                       #
# Copyright 2018 Anton Nguyen <afnguyen85@gmail.com>                           #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Jasper van Wanrooy <jasper@vanwanrooy.net>                    #
# Copyright 2018 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Tim Boring <tboring@hearst.com>                               #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Brian Choy <byceee@gmail.com>                                 #
# Copyright 2019 Geoffroy Jabouley <gjabouley@invensense.com>                  #
# Copyright 2019 Pascal Bach <pasci.bach@gmail.com>                            #
# Copyright 2019 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2019 Shibasis Patel <smartshibasish@gmail.com>                     #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2019 ebrown <brownierin@users.noreply.github.com>                  #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
# Copyright 2020 Glenn McDonald <testworksau@users.noreply.github.com>         #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 latacora-daniel <71085674+latacora-daniel@users.noreply.github.com>#
# Copyright 2020 ton-katsu <sakamoto.yoshihisa@gmail.com>                      #
# Copyright 2021 James Simpson <jsimpso@users.noreply.github.com>              #
# Copyright 2021 Marina Peresypkina <mi9onev@gmail.com>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Tanner <51724788+lightningboltemoji@users.noreply.github.com> #
# Copyright 2022 KimSia Sim <245021+simkimsia@users.noreply.github.com>        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Felipe Peter <mr-peipei@web.de>                               #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Greg <31892308+jmgreg31@users.noreply.github.com>    #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Mark Amery <markamery@btinternet.com>                         #
# Copyright 2023 Mauricio Alejandro Martínez Pacheco <mauricio.martinez@premise.com>#
# Copyright 2023 Mauricio Alejandro Martínez Pacheco <n_othing@hotmail.com>    #
# Copyright 2023 Oliver Mannion <125105+tekumara@users.noreply.github.com>     #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Andrii Kezikov <cheshirez@gmail.com>                          #
# Copyright 2024 Mohamed Mostafa <112487260+mohy01@users.noreply.github.com>   #
# Copyright 2024 Oskar Jansson <56458534+janssonoskar@users.noreply.github.com>#
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

import urllib.parse
from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.Event
import github.GithubObject
import github.HookDelivery
import github.NamedUser
import github.OrganizationDependabotAlert
import github.OrganizationSecret
import github.OrganizationVariable
import github.Plan
import github.Project
import github.Repository
import github.Team
from github import Consts
from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.Event import Event
    from github.Hook import Hook
    from github.Installation import Installation
    from github.Issue import Issue
    from github.Label import Label
    from github.Migration import Migration
    from github.NamedUser import NamedUser
    from github.OrganizationDependabotAlert import OrganizationDependabotAlert
    from github.OrganizationSecret import OrganizationSecret
    from github.OrganizationVariable import OrganizationVariable
    from github.Plan import Plan
    from github.Project import Project
    from github.PublicKey import PublicKey
    from github.Repository import Repository
    from github.Team import Team


class Organization(CompletableGithubObject):
    """
    This class represents Organizations.

    The reference can be found here
    https://docs.github.com/en/rest/reference/orgs

    """

    def _initAttributes(self) -> None:
        self._default_repository_permission: Attribute[str] = NotSet
        self._has_organization_projects: Attribute[bool] = NotSet
        self._has_repository_projects: Attribute[bool] = NotSet
        self._hooks_url: Attribute[str] = NotSet
        self._issues_url: Attribute[str] = NotSet
        self._members_can_create_repositories: Attribute[bool] = NotSet
        self._two_factor_requirement_enabled: Attribute[bool] = NotSet
        self._avatar_url: Attribute[str] = NotSet
        self._billing_email: Attribute[str] = NotSet
        self._blog: Attribute[str | None] = NotSet
        self._collaborators: Attribute[int] = NotSet
        self._company: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._disk_usage: Attribute[int] = NotSet
        self._email: Attribute[str] = NotSet
        self._events_url: Attribute[str] = NotSet
        self._followers: Attribute[int] = NotSet
        self._following: Attribute[int] = NotSet
        self._gravatar_id: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._location: Attribute[str] = NotSet
        self._login: Attribute[str] = NotSet
        self._members_url: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._owned_private_repos: Attribute[int] = NotSet
        self._plan: Attribute[Plan] = NotSet
        self._private_gists: Attribute[int] = NotSet
        self._public_gists: Attribute[int] = NotSet
        self._public_members_url: Attribute[str] = NotSet
        self._public_repos: Attribute[int] = NotSet
        self._repos_url: Attribute[str] = NotSet
        self._total_private_repos: Attribute[int] = NotSet
        self._type: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"login": self._login.value})

    @property
    def avatar_url(self) -> str:
        self._completeIfNotSet(self._avatar_url)
        return self._avatar_url.value

    @property
    def billing_email(self) -> str:
        self._completeIfNotSet(self._billing_email)
        return self._billing_email.value

    @property
    def blog(self) -> str | None:
        self._completeIfNotSet(self._blog)
        return self._blog.value

    @property
    def collaborators(self) -> int:
        self._completeIfNotSet(self._collaborators)
        return self._collaborators.value

    @property
    def company(self) -> str | None:
        self._completeIfNotSet(self._company)
        return self._company.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def default_repository_permission(self) -> str:
        self._completeIfNotSet(self._default_repository_permission)
        return self._default_repository_permission.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def disk_usage(self) -> int:
        self._completeIfNotSet(self._disk_usage)
        return self._disk_usage.value

    @property
    def email(self) -> str | None:
        self._completeIfNotSet(self._email)
        return self._email.value

    @property
    def events_url(self) -> str:
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def followers(self) -> int:
        self._completeIfNotSet(self._followers)
        return self._followers.value

    @property
    def following(self) -> int:
        self._completeIfNotSet(self._following)
        return self._following.value

    @property
    def gravatar_id(self) -> str:
        self._completeIfNotSet(self._gravatar_id)
        return self._gravatar_id.value

    @property
    def has_organization_projects(self) -> bool:
        self._completeIfNotSet(self._has_organization_projects)
        return self._has_organization_projects.value

    @property
    def has_repository_projects(self) -> bool:
        self._completeIfNotSet(self._has_repository_projects)
        return self._has_repository_projects.value

    @property
    def hooks_url(self) -> str:
        self._completeIfNotSet(self._hooks_url)
        return self._hooks_url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def issues_url(self) -> str:
        self._completeIfNotSet(self._issues_url)
        return self._issues_url.value

    @property
    def location(self) -> str:
        self._completeIfNotSet(self._location)
        return self._location.value

    @property
    def login(self) -> str:
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def members_can_create_repositories(self) -> bool:
        self._completeIfNotSet(self._members_can_create_repositories)
        return self._members_can_create_repositories.value

    @property
    def members_url(self) -> str:
        self._completeIfNotSet(self._members_url)
        return self._members_url.value

    @property
    def name(self) -> str | None:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def owned_private_repos(self) -> int:
        self._completeIfNotSet(self._owned_private_repos)
        return self._owned_private_repos.value

    @property
    def plan(self) -> Plan:
        self._completeIfNotSet(self._plan)
        return self._plan.value

    @property
    def private_gists(self) -> int:
        self._completeIfNotSet(self._private_gists)
        return self._private_gists.value

    @property
    def public_gists(self) -> int:
        self._completeIfNotSet(self._public_gists)
        return self._public_gists.value

    @property
    def public_members_url(self) -> str:
        self._completeIfNotSet(self._public_members_url)
        return self._public_members_url.value

    @property
    def public_repos(self) -> int:
        self._completeIfNotSet(self._public_repos)
        return self._public_repos.value

    @property
    def repos_url(self) -> str:
        self._completeIfNotSet(self._repos_url)
        return self._repos_url.value

    @property
    def total_private_repos(self) -> int:
        self._completeIfNotSet(self._total_private_repos)
        return self._total_private_repos.value

    @property
    def two_factor_requirement_enabled(self) -> bool:
        self._completeIfNotSet(self._two_factor_requirement_enabled)
        return self._two_factor_requirement_enabled.value

    @property
    def type(self) -> str:
        self._completeIfNotSet(self._type)
        return self._type.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def add_to_members(self, member: NamedUser, role: Opt[str] = NotSet) -> None:
        """
        :calls: `PUT /orgs/{org}/memberships/{user} <https://docs.github.com/en/rest/reference/orgs#update-an-organization-membership-for-the-authenticated-user>`_
        """
        assert is_optional(role, str), role
        assert isinstance(member, github.NamedUser.NamedUser), member
        put_parameters = NotSet.remove_unset_items({"role": role})
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/memberships/{member._identity}", input=put_parameters
        )

    def add_to_public_members(self, public_member: NamedUser) -> None:
        """
        :calls: `PUT /orgs/{org}/public_members/{user} <https://docs.github.com/en/rest/reference/orgs#members>`_
        """
        assert isinstance(public_member, github.NamedUser.NamedUser), public_member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/public_members/{public_member._identity}"
        )

    def create_fork(
        self,
        repo: Repository,
        name: Opt[str] = NotSet,
        default_branch_only: Opt[bool] = NotSet,
    ) -> Repository:
        """
        :calls: `POST /repos/{owner}/{repo}/forks <https://docs.github.com/en/rest/reference/repos#forks>`_
        """
        assert isinstance(repo, github.Repository.Repository), repo
        return repo.create_fork(
            self,
            name=name,
            default_branch_only=default_branch_only,
        )

    def create_repo_from_template(
        self,
        name: str,
        repo: Repository,
        description: Opt[str] = NotSet,
        include_all_branches: Opt[bool] = NotSet,
        private: Opt[bool] = NotSet,
    ) -> Repository:
        """self.name
        :calls: `POST /repos/{template_owner}/{template_repo}/generate <https://docs.github.com/en/rest/reference/repos#create-a-repository-using-a-template>`_
        """
        assert isinstance(name, str), name
        assert isinstance(repo, github.Repository.Repository), repo
        assert is_optional(description, str), description
        assert is_optional(include_all_branches, bool), include_all_branches
        assert is_optional(private, bool), private
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "name": name,
                "owner": self.login,
                "description": description,
                "include_all_branches": include_all_branches,
                "private": private,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"/repos/{repo.owner.login}/{repo.name}/generate",
            input=post_parameters,
            headers={"Accept": "application/vnd.github.v3+json"},
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def create_hook(
        self,
        name: str,
        config: dict[str, str],
        events: Opt[list[str]] = NotSet,
        active: Opt[bool] = NotSet,
    ) -> Hook:
        """
        :calls: `POST /orgs/{owner}/hooks <https://docs.github.com/en/rest/reference/orgs#webhooks>`_
        :param name: string
        :param config: dict
        :param events: list of string
        :param active: bool
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(name, str), name
        assert isinstance(config, dict), config
        assert is_optional_list(events, str), events
        assert is_optional(active, bool), active
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "name": name,
                "config": config,
                "events": events,
                "active": active,
            }
        )
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/hooks", input=post_parameters)
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def create_project(self, name: str, body: Opt[str] = NotSet) -> github.Project.Project:
        """
        :calls: `POST /orgs/{org}/projects <https://docs.github.com/en/rest/reference/projects#create-an-organization-project>`_
        """
        assert isinstance(name, str), name
        assert is_optional(body, str), body
        post_parameters: dict[str, Any] = NotSet.remove_unset_items({"name": name, "body": body})

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/projects",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return github.Project.Project(self._requester, headers, data, completed=True)

    def create_repo(
        self,
        name: str,
        description: Opt[str] = NotSet,
        homepage: Opt[str] = NotSet,
        private: Opt[bool] = NotSet,
        visibility: Opt[str] = NotSet,
        has_issues: Opt[bool] = NotSet,
        has_wiki: Opt[bool] = NotSet,
        has_downloads: Opt[bool] = NotSet,
        has_projects: Opt[bool] = NotSet,
        team_id: Opt[int] = NotSet,
        auto_init: Opt[bool] = NotSet,
        license_template: Opt[str] = NotSet,
        gitignore_template: Opt[str] = NotSet,
        allow_squash_merge: Opt[bool] = NotSet,
        allow_merge_commit: Opt[bool] = NotSet,
        allow_rebase_merge: Opt[bool] = NotSet,
        delete_branch_on_merge: Opt[bool] = NotSet,
        allow_update_branch: Opt[bool] = NotSet,
        is_template: Opt[bool] = NotSet,
        allow_auto_merge: Opt[bool] = NotSet,
        use_squash_pr_title_as_default: Opt[bool] = NotSet,
        squash_merge_commit_title: Opt[str] = NotSet,
        squash_merge_commit_message: Opt[str] = NotSet,
        merge_commit_title: Opt[str] = NotSet,
        merge_commit_message: Opt[str] = NotSet,
        custom_properties: Opt[dict[str, Any]] = NotSet,
    ) -> github.Repository.Repository:
        """
        :calls: `POST /orgs/{org}/repos <https://docs.github.com/en/rest/reference/repos>`_
        """
        assert isinstance(name, str), name
        assert is_optional(description, str), description
        assert is_optional(homepage, str), homepage
        assert is_optional(private, bool), private
        assert is_optional(visibility, str), visibility
        assert is_optional(has_issues, bool), has_issues
        assert is_optional(has_wiki, bool), has_wiki
        assert is_optional(has_downloads, bool), has_downloads
        assert is_optional(has_projects, bool), has_projects
        assert is_optional(team_id, int), team_id
        assert is_optional(auto_init, bool), auto_init
        assert is_optional(license_template, str), license_template
        assert is_optional(gitignore_template, str), gitignore_template
        assert is_optional(allow_squash_merge, bool), allow_squash_merge
        assert is_optional(allow_merge_commit, bool), allow_merge_commit
        assert is_optional(allow_rebase_merge, bool), allow_rebase_merge
        assert is_optional(delete_branch_on_merge, bool), delete_branch_on_merge
        assert is_optional(allow_update_branch, bool), allow_update_branch
        assert is_optional(is_template, bool), is_template
        assert is_optional(allow_auto_merge, bool), allow_auto_merge
        assert is_optional(use_squash_pr_title_as_default, bool), use_squash_pr_title_as_default
        assert squash_merge_commit_title in ["PR_TITLE", "COMMIT_OR_PR_TITLE", NotSet], squash_merge_commit_title
        assert squash_merge_commit_message in [
            "PR_BODY",
            "COMMIT_MESSAGES",
            "BLANK",
            NotSet,
        ], squash_merge_commit_message
        assert merge_commit_title in ["PR_TITLE", "MERGE_MESSAGE", NotSet], merge_commit_title
        assert merge_commit_message in ["PR_TITLE", "PR_BODY", "BLANK", NotSet], merge_commit_message
        assert is_optional(custom_properties, dict), custom_properties
        post_parameters = NotSet.remove_unset_items(
            {
                "name": name,
                "description": description,
                "homepage": homepage,
                "private": private,
                "visibility": visibility,
                "has_issues": has_issues,
                "has_wiki": has_wiki,
                "has_downloads": has_downloads,
                "has_projects": has_projects,
                "team_id": team_id,
                "auto_init": auto_init,
                "license_template": license_template,
                "gitignore_template": gitignore_template,
                "allow_squash_merge": allow_squash_merge,
                "allow_merge_commit": allow_merge_commit,
                "allow_rebase_merge": allow_rebase_merge,
                "delete_branch_on_merge": delete_branch_on_merge,
                "allow_update_branch": allow_update_branch,
                "is_template": is_template,
                "allow_auto_merge": allow_auto_merge,
                "use_squash_pr_title_as_default": use_squash_pr_title_as_default,
                "squash_merge_commit_title": squash_merge_commit_title,
                "squash_merge_commit_message": squash_merge_commit_message,
                "merge_commit_title": merge_commit_title,
                "merge_commit_message": merge_commit_message,
                "custom_properties": custom_properties,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/repos",
            input=post_parameters,
            headers={"Accept": Consts.repoVisibilityPreview},
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def create_secret(
        self,
        secret_name: str,
        unencrypted_value: str,
        visibility: str = "all",
        selected_repositories: Opt[list[github.Repository.Repository]] = NotSet,
    ) -> github.OrganizationSecret.OrganizationSecret:
        """
        :calls: `PUT /orgs/{org}/actions/secrets/{secret_name} <https://docs.github.com/en/rest/actions/secrets#create-or-update-an-organization-secret>`_
        """
        assert isinstance(secret_name, str), secret_name
        assert isinstance(unencrypted_value, str), unencrypted_value
        assert isinstance(visibility, str), visibility
        if visibility == "selected":
            assert isinstance(selected_repositories, list) and all(
                isinstance(element, github.Repository.Repository) for element in selected_repositories
            ), selected_repositories
        else:
            assert selected_repositories is NotSet

        public_key = self.get_public_key()
        payload = public_key.encrypt(unencrypted_value)
        put_parameters: dict[str, Any] = {
            "key_id": public_key.key_id,
            "encrypted_value": payload,
            "visibility": visibility,
        }
        if is_defined(selected_repositories):
            put_parameters["selected_repository_ids"] = [element.id for element in selected_repositories]

        self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/actions/secrets/{urllib.parse.quote(secret_name)}", input=put_parameters
        )

        return github.OrganizationSecret.OrganizationSecret(
            requester=self._requester,
            headers={},
            attributes={
                "name": secret_name,
                "visibility": visibility,
                "selected_repositories_url": f"{self.url}/actions/secrets/{urllib.parse.quote(secret_name)}/repositories",
                "url": f"{self.url}/actions/secrets/{urllib.parse.quote(secret_name)}",
            },
            completed=False,
        )

    def get_secrets(self, secret_type: str = "actions") -> PaginatedList[OrganizationSecret]:
        """
        Gets all organization secrets :param secret_type: string options actions or dependabot :rtype:

        :class:`PaginatedList` of :class:`github.OrganizationSecret.OrganizationSecret`

        """
        assert secret_type in ["actions", "dependabot"], "secret_type should be actions or dependabot"
        return PaginatedList(
            github.OrganizationSecret.OrganizationSecret,
            self._requester,
            f"{self.url}/{secret_type}/secrets",
            None,
            list_item="secrets",
        )

    def get_secret(self, secret_name: str, secret_type: str = "actions") -> OrganizationSecret:
        """
        :calls: 'GET /orgs/{org}/{secret_type}/secrets/{secret_name} <https://docs.github.com/en/rest/actions/secrets#get-an-organization-secret>`_
        :param secret_name: string
        :param secret_type: string options actions or dependabot
        :rtype: github.OrganizationSecret.OrganizationSecret
        """
        assert isinstance(secret_name, str), secret_name
        return github.OrganizationSecret.OrganizationSecret(
            requester=self._requester,
            headers={},
            attributes={"url": f"{self.url}/{secret_type}/secrets/{urllib.parse.quote(secret_name)}"},
            completed=False,
        )

    def create_team(
        self,
        name: str,
        repo_names: Opt[list[Repository]] = NotSet,
        permission: Opt[str] = NotSet,
        privacy: Opt[str] = NotSet,
        description: Opt[str] = NotSet,
        parent_team_id: Opt[int] = NotSet,
        maintainers: Opt[list[int]] = NotSet,
        notification_setting: Opt[str] = NotSet,
    ) -> Team:
        """
        :calls: `POST /orgs/{org}/teams <https://docs.github.com/en/rest/reference/teams#list-teams>`_
        :param name: string
        :param repo_names: list of :class:`github.Repository.Repository`
        :param permission: string
        :param privacy: string
        :param description: string
        :param parent_team_id: integer
        :param maintainers: list of: integer
        :param notification_setting: string
        :rtype: :class:`github.Team.Team`
        """
        assert isinstance(name, str), name
        assert is_optional_list(repo_names, github.Repository.Repository), repo_names
        assert is_optional_list(maintainers, int), maintainers
        assert is_optional(parent_team_id, int), parent_team_id
        assert is_optional(permission, str), permission
        assert is_optional(privacy, str), privacy
        assert is_optional(description, str), description
        assert notification_setting in ["notifications_enabled", "notifications_disabled", NotSet], notification_setting
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "name": name,
                "permission": permission,
                "privacy": privacy,
                "description": description,
                "parent_team_id": parent_team_id,
                "maintainers": maintainers,
                "notification_setting": notification_setting,
            }
        )
        if is_defined(repo_names):
            post_parameters["repo_names"] = [element._identity for element in repo_names]
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/teams", input=post_parameters)
        return github.Team.Team(self._requester, headers, data, completed=True)

    def create_variable(
        self,
        variable_name: str,
        value: str,
        visibility: str = "all",
        selected_repositories: github.GithubObject.Opt[list[github.Repository.Repository]] = NotSet,
    ) -> github.OrganizationVariable.OrganizationVariable:
        """
        :calls: `POST /orgs/{org}/actions/variables/ <https://docs.github.com/en/rest/actions/variables#create-an-organization-variable>`_
        :param variable_name: string
        :param value: string
        :param visibility: string
        :param selected_repositories: list of :class:`github.Repository.Repository`
        :rtype: github.OrganizationVariable.OrganizationVariable
        """
        assert isinstance(variable_name, str), variable_name
        assert isinstance(value, str), value
        assert isinstance(visibility, str), visibility
        if visibility == "selected":
            assert isinstance(selected_repositories, list) and all(
                isinstance(element, github.Repository.Repository) for element in selected_repositories
            ), selected_repositories
        else:
            assert selected_repositories is NotSet

        post_parameters: dict[str, Any] = {
            "name": variable_name,
            "value": value,
            "visibility": visibility,
        }
        if is_defined(selected_repositories):
            post_parameters["selected_repository_ids"] = [element.id for element in selected_repositories]

        self._requester.requestJsonAndCheck("POST", f"{self.url}/actions/variables", input=post_parameters)

        return github.OrganizationVariable.OrganizationVariable(
            requester=self._requester,
            headers={},
            attributes={
                "name": variable_name,
                "visibility": visibility,
                "value": value,
                "selected_repositories_url": f"{self.url}/actions/variables/{urllib.parse.quote(variable_name)}/repositories",
                "url": self.url,
            },
            completed=False,
        )

    def get_variables(self) -> PaginatedList[OrganizationVariable]:
        """
        Gets all organization variables :rtype: :class:`PaginatedList` of
        :class:`github.OrganizationVariable.OrganizationVariable`
        """
        return PaginatedList(
            github.OrganizationVariable.OrganizationVariable,
            self._requester,
            f"{self.url}/actions/variables",
            None,
            list_item="variables",
        )

    def get_variable(self, variable_name: str) -> OrganizationVariable:
        """
        :calls: 'GET /orgs/{org}/actions/variables/{variable_name} <https://docs.github.com/en/rest/actions/variables#get-an-organization-variable>`_
        :param variable_name: string
        :rtype: github.OrganizationVariable.OrganizationVariable
        """
        assert isinstance(variable_name, str), variable_name
        return github.OrganizationVariable.OrganizationVariable(
            requester=self._requester,
            headers={},
            attributes={"url": f"{self.url}/actions/variables/{urllib.parse.quote(variable_name)}"},
            completed=False,
        )

    def delete_hook(self, id: int) -> None:
        """
        :calls: `DELETE /orgs/{owner}/hooks/{id} <https://docs.github.com/en/rest/reference/orgs#webhooks>`_
        :param id: integer
        :rtype: None`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/hooks/{id}")

    def edit(
        self,
        billing_email: Opt[str] = NotSet,
        blog: Opt[str] = NotSet,
        company: Opt[str] = NotSet,
        description: Opt[str] = NotSet,
        email: Opt[str] = NotSet,
        location: Opt[str] = NotSet,
        name: Opt[str] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /orgs/{org} <https://docs.github.com/en/rest/reference/orgs>`_
        """
        assert is_optional(billing_email, str), billing_email
        assert is_optional(blog, str), blog
        assert is_optional(company, str), company
        assert is_optional(description, str), description
        assert is_optional(email, str), email
        assert is_optional(location, str), location
        assert is_optional(name, str), name
        post_parameters = NotSet.remove_unset_items(
            {
                "billing_email": billing_email,
                "blog": blog,
                "company": company,
                "description": description,
                "email": email,
                "location": location,
                "name": name,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def edit_hook(
        self,
        id: int,
        name: str,
        config: dict[str, str],
        events: Opt[list[str]] = NotSet,
        active: Opt[bool] = NotSet,
    ) -> Hook:
        """
        :calls: `PATCH /orgs/{owner}/hooks/{id} <https://docs.github.com/en/rest/reference/orgs#webhooks>`_
        """
        assert isinstance(id, int), id
        assert isinstance(name, str), name
        assert isinstance(config, dict), config
        assert is_optional_list(events, str), events
        assert is_optional(active, bool), active
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {"name": name, "config": config, "events": events, "active": active}
        )

        headers, data = self._requester.requestJsonAndCheck("PATCH", f"{self.url}/hooks/{id}", input=post_parameters)
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def get_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /orgs/{org}/events <https://docs.github.com/en/rest/reference/activity#events>`_
        :rtype: :class:`PaginatedList` of :class:`github.Event.Event`
        """
        return PaginatedList(github.Event.Event, self._requester, f"{self.url}/events", None)

    def get_hook(self, id: int) -> github.Hook.Hook:
        """
        :calls: `GET /orgs/{owner}/hooks/{id} <https://docs.github.com/en/rest/reference/orgs#webhooks>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/hooks/{id}")
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def get_hooks(self) -> PaginatedList[Hook]:
        """
        :calls: `GET /orgs/{owner}/hooks <https://docs.github.com/en/rest/reference/orgs#webhooks>`_
        """
        return PaginatedList(github.Hook.Hook, self._requester, f"{self.url}/hooks", None)

    def get_hook_delivery(self, hook_id: int, delivery_id: int) -> github.HookDelivery.HookDelivery:
        """
        :calls: `GET /orgs/{owner}/hooks/{hook_id}/deliveries/{delivery_id} <https://docs.github.com/en/rest/reference/orgs#get-a-webhook-delivery-for-an-organization-webhook>`_
        :param hook_id: integer
        :param delivery_id: integer
        :rtype: :class:`github.HookDelivery.HookDelivery`
        """
        assert isinstance(hook_id, int), hook_id
        assert isinstance(delivery_id, int), delivery_id
        headers, data = self._requester.requestJsonAndCheck(
            "GET", f"{self.url}/hooks/{hook_id}/deliveries/{delivery_id}"
        )
        return github.HookDelivery.HookDelivery(self._requester, headers, data, completed=True)

    def get_hook_deliveries(self, hook_id: int) -> PaginatedList[github.HookDelivery.HookDeliverySummary]:
        """
        :calls: `GET /orgs/{owner}/hooks/{hook_id}/deliveries <https://docs.github.com/en/rest/reference/orgs#list-deliveries-for-an-organization-webhook>`_
        :param hook_id: integer
        :rtype: :class:`PaginatedList` of :class:`github.HookDelivery.HookDeliverySummary`
        """
        assert isinstance(hook_id, int), hook_id
        return PaginatedList(
            github.HookDelivery.HookDeliverySummary,
            self._requester,
            f"{self.url}/hooks/{hook_id}/deliveries",
            None,
        )

    def get_issues(
        self,
        filter: Opt[str] = NotSet,
        state: Opt[str] = NotSet,
        labels: Opt[list[Label]] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
        since: Opt[datetime] = NotSet,
    ) -> PaginatedList[Issue]:
        """
        :calls: `GET /orgs/{org}/issues <https://docs.github.com/en/rest/reference/issues>`_
        :rtype: :class:`PaginatedList` of :class:`github.Issue.Issue`
        :param filter: string
        :param state: string
        :param labels: list of :class:`github.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime
        :rtype: :class:`PaginatedList` of :class:`github.Issue.Issue`
        """
        assert is_optional(filter, str), filter
        assert is_optional(state, str), state
        assert is_optional_list(labels, github.Label.Label), labels
        assert is_optional(sort, str), sort
        assert is_optional(direction, str), direction
        assert is_optional(since, datetime), since
        url_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {"filter": filter, "state": state, "sort": sort, "direction": direction}
        )
        if is_defined(labels):
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return PaginatedList(github.Issue.Issue, self._requester, f"{self.url}/issues", url_parameters)

    def get_members(
        self,
        filter_: Opt[str] = NotSet,
        role: Opt[str] = NotSet,
    ) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /orgs/{org}/members <https://docs.github.com/en/rest/reference/orgs#members>`_
        """
        assert is_optional(filter_, str), filter_
        assert is_optional(role, str), role

        url_parameters = NotSet.remove_unset_items({"filter": filter_, "role": role})

        return PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.url}/members",
            url_parameters,
        )

    def get_projects(self, state: Opt[str] = NotSet) -> PaginatedList[Project]:
        """
        :calls: `GET /orgs/{org}/projects <https://docs.github.com/en/rest/reference/projects#list-organization-projects>`_
        """

        url_parameters = NotSet.remove_unset_items({"state": state})

        return PaginatedList(
            github.Project.Project,
            self._requester,
            f"{self.url}/projects",
            url_parameters,
            {"Accept": Consts.mediaTypeProjectsPreview},
        )

    def get_public_members(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /orgs/{org}/public_members <https://docs.github.com/en/rest/reference/orgs#members>`_
        :rtype: :class:`PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.url}/public_members",
            None,
        )

    def get_outside_collaborators(self, filter_: Opt[str] = NotSet) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /orgs/{org}/outside_collaborators <https://docs.github.com/en/rest/reference/orgs#outside-collaborators>`_
        """
        assert is_optional(filter_, str), filter_

        url_parameters = NotSet.remove_unset_items({"filter": filter_})
        return PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.url}/outside_collaborators",
            url_parameters,
        )

    def remove_outside_collaborator(self, collaborator: NamedUser) -> None:
        """
        :calls: `DELETE /orgs/{org}/outside_collaborators/{username} <https://docs.github.com/en/rest/reference/orgs#outside-collaborators>`_
        :param collaborator: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser), collaborator
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.url}/outside_collaborators/{collaborator._identity}"
        )

    def convert_to_outside_collaborator(self, member: NamedUser) -> None:
        """
        :calls: `PUT /orgs/{org}/outside_collaborators/{username} <https://docs.github.com/en/rest/reference/orgs#outside-collaborators>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/outside_collaborators/{member._identity}"
        )

    def get_public_key(self) -> PublicKey:
        """
        :calls: `GET /orgs/{org}/actions/secrets/public-key <https://docs.github.com/en/rest/reference/actions#get-an-organization-public-key>`_
        :rtype: :class:`github.PublicKey.PublicKey`
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/actions/secrets/public-key")
        return github.PublicKey.PublicKey(self._requester, headers, data, completed=True)

    def get_repo(self, name: str) -> Repository:
        """
        :calls: `GET /repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/repos>`_
        :param name: string
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(name, str), name
        name = urllib.parse.quote(name)
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            f"/repos/{self.login}/{name}",
            headers={"Accept": Consts.repoVisibilityPreview},
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def get_repos(
        self,
        type: Opt[str] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
    ) -> PaginatedList[Repository]:
        """
        :calls: `GET /orgs/{org}/repos <https://docs.github.com/en/rest/reference/repos>`_
        :param type: string ('all', 'public', 'private', 'forks', 'sources', 'member')
        :param sort: string ('created', 'updated', 'pushed', 'full_name')
        :param direction: string ('asc', desc')
        """
        assert is_optional(type, str), type
        assert is_optional(sort, str), sort
        assert is_optional(direction, str), direction

        url_parameters = NotSet.remove_unset_items({"type": type, "sort": sort, "direction": direction})

        return PaginatedList(
            github.Repository.Repository,
            self._requester,
            f"{self.url}/repos",
            url_parameters,
            headers={"Accept": Consts.repoVisibilityPreview},
        )

    def get_team(self, id: int) -> Team:
        """
        :calls: `GET /teams/{id} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"/teams/{id}")
        return github.Team.Team(self._requester, headers, data, completed=True)

    def get_team_by_slug(self, slug: str) -> Team:
        """
        :calls: `GET /orgs/{org}/teams/{team_slug} <https://docs.github.com/en/rest/reference/teams#get-a-team-by-name>`_
        """
        assert isinstance(slug, str), slug
        slug = urllib.parse.quote(slug)
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/teams/{slug}")
        return github.Team.Team(self._requester, headers, data, completed=True)

    def get_teams(self) -> PaginatedList[Team]:
        """
        :calls: `GET /orgs/{org}/teams <https://docs.github.com/en/rest/reference/teams#list-teams>`_
        """
        return PaginatedList(github.Team.Team, self._requester, f"{self.url}/teams", None)

    def invitations(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /orgs/{org}/invitations <https://docs.github.com/en/rest/reference/orgs#members>`_
        """
        return PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.url}/invitations",
            None,
            headers={"Accept": Consts.mediaTypeOrganizationInvitationPreview},
        )

    def invite_user(
        self,
        user: Opt[NamedUser] = NotSet,
        email: Opt[str] = NotSet,
        role: Opt[str] = NotSet,
        teams: Opt[list[Team]] = NotSet,
    ) -> None:
        """
        :calls: `POST /orgs/{org}/invitations <https://docs.github.com/en/rest/reference/orgs#members>`_
        :param user: :class:`github.NamedUser.NamedUser`
        :param email: string
        :param role: string
        :param teams: array of :class:`github.Team.Team`
        :rtype: None
        """
        assert is_optional(user, github.NamedUser.NamedUser), user
        assert is_optional(email, str), email
        assert is_defined(email) != is_defined(user), "specify only one of email or user"

        assert is_undefined(role) or role in ["admin", "direct_member", "billing_manager"], role
        assert is_optional_list(teams, github.Team.Team), teams

        parameters: dict[str, Any] = NotSet.remove_unset_items({"email": email, "role": role})

        if is_defined(user):
            parameters["invitee_id"] = user.id
        if is_defined(teams):
            parameters["team_ids"] = [t.id for t in teams]

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/invitations",
            headers={"Accept": Consts.mediaTypeOrganizationInvitationPreview},
            input=parameters,
        )

    def cancel_invitation(self, invitee: NamedUser) -> bool:
        """
        :calls: `DELETE /orgs/{org}/invitations/{invitation_id} <https://docs.github.com/en/rest/reference/orgs#cancel-an-organization-invitation>`_
        :param invitee: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(invitee, github.NamedUser.NamedUser), invitee
        status, headers, data = self._requester.requestJson("DELETE", f"{self.url}/invitations/{invitee.id}")
        return status == 204

    def has_in_members(self, member: NamedUser) -> bool:
        """
        :calls: `GET /orgs/{org}/members/{user} <https://docs.github.com/en/rest/reference/orgs#members>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        status, headers, data = self._requester.requestJson("GET", f"{self.url}/members/{member._identity}")
        if status == 302:
            status, headers, data = self._requester.requestJson("GET", headers["location"])
        return status == 204

    def has_in_public_members(self, public_member: NamedUser) -> bool:
        """
        :calls: `GET /orgs/{org}/public_members/{user} <https://docs.github.com/en/rest/reference/orgs#members>`_
        :param public_member: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(public_member, github.NamedUser.NamedUser), public_member
        status, headers, data = self._requester.requestJson(
            "GET", f"{self.url}/public_members/{public_member._identity}"
        )
        return status == 204

    def remove_from_membership(self, member: NamedUser) -> None:
        """
        :calls: `DELETE /orgs/{org}/memberships/{user} <https://docs.github.com/en/rest/reference/orgs#remove-an-organization-member>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/memberships/{member._identity}")

    def remove_from_members(self, member: NamedUser) -> None:
        """
        :calls: `DELETE /orgs/{org}/members/{user} <https://docs.github.com/en/rest/reference/orgs#members>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/members/{member._identity}")

    def remove_from_public_members(self, public_member: NamedUser) -> None:
        """
        :calls: `DELETE /orgs/{org}/public_members/{user} <https://docs.github.com/en/rest/reference/orgs#members>`_
        :param public_member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(public_member, github.NamedUser.NamedUser), public_member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.url}/public_members/{public_member._identity}"
        )

    def create_migration(
        self,
        repos: list[str],
        lock_repositories: Opt[bool] = NotSet,
        exclude_attachments: Opt[bool] = NotSet,
    ) -> Migration:
        """
        :calls: `POST /orgs/{org}/migrations <https://docs.github.com/en/rest/reference/migrations#list-organization-migrations>`_
        :param repos: list or tuple of str
        :param lock_repositories: bool
        :param exclude_attachments: bool
        :rtype: :class:`github.Migration.Migration`
        """
        assert isinstance(repos, (list, tuple)), repos
        assert all(isinstance(repo, str) for repo in repos), repos
        assert is_optional(lock_repositories, bool), lock_repositories
        assert is_optional(exclude_attachments, bool), exclude_attachments
        post_parameters = NotSet.remove_unset_items(
            {
                "repositories": repos,
                "lock_repositories": lock_repositories,
                "exclude_attachments": exclude_attachments,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"/orgs/{self.login}/migrations",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeMigrationPreview},
        )
        return github.Migration.Migration(self._requester, headers, data, completed=True)

    def get_migrations(self) -> PaginatedList[Migration]:
        """
        :calls: `GET /orgs/{org}/migrations <https://docs.github.com/en/rest/reference/migrations#list-organization-migrations>`_
        :rtype: :class:`PaginatedList` of :class:`github.Migration.Migration`
        """
        return PaginatedList(
            github.Migration.Migration,
            self._requester,
            f"/orgs/{self.login}/migrations",
            None,
            headers={"Accept": Consts.mediaTypeMigrationPreview},
        )

    def get_installations(self) -> PaginatedList[Installation]:
        """
        :calls: `GET /orgs/{org}/installations <https://docs.github.com/en/rest/reference/orgs#list-app-installations-for-an-organization>`_
        :rtype: :class:`PaginatedList` of :class:`github.Installation.Installation`
        """

        return PaginatedList(
            github.Installation.Installation,
            self._requester,
            f"{self.url}/installations",
            None,
            None,
            list_item="installations",
        )

    def get_dependabot_alerts(
        self,
        state: Opt[str] = NotSet,
        severity: Opt[str] = NotSet,
        ecosystem: Opt[str] = NotSet,
        package: Opt[str] = NotSet,
        scope: Opt[str] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
    ) -> PaginatedList[OrganizationDependabotAlert]:
        """
        :calls: `GET /orgs/{org}/dependabot/alerts <https://docs.github.com/en/rest/dependabot/alerts#list-dependabot-alerts-for-an-organization>`_
        :param state: Optional string
        :param severity: Optional string
        :param ecosystem: Optional string
        :param package: Optional string
        :param scope: Optional string
        :param sort: Optional string
        :param direction: Optional string
        :rtype: :class:`PaginatedList` of :class:`github.DependabotAlert.DependabotAlert`
        """
        allowed_states = ["auto_dismissed", "dismissed", "fixed", "open"]
        allowed_severities = ["low", "medium", "high", "critical"]
        allowed_ecosystems = ["composer", "go", "maven", "npm", "nuget", "pip", "pub", "rubygems", "rust"]
        allowed_scopes = ["development", "runtime"]
        allowed_sorts = ["created", "updated"]
        allowed_directions = ["asc", "desc"]
        assert state in allowed_states + [NotSet], f"State can be one of {', '.join(allowed_states)}"
        assert severity in allowed_severities + [NotSet], f"Severity can be one of {', '.join(allowed_severities)}"
        assert ecosystem in allowed_ecosystems + [NotSet], f"Ecosystem can be one of {', '.join(allowed_ecosystems)}"
        assert scope in allowed_scopes + [NotSet], f"Scope can be one of {', '.join(allowed_scopes)}"
        assert sort in allowed_sorts + [NotSet], f"Sort can be one of {', '.join(allowed_sorts)}"
        assert direction in allowed_directions + [NotSet], f"Direction can be one of {', '.join(allowed_directions)}"
        url_parameters = NotSet.remove_unset_items(
            {
                "state": state,
                "severity": severity,
                "ecosystem": ecosystem,
                "package": package,
                "scope": scope,
                "sort": sort,
                "direction": direction,
            }
        )
        return PaginatedList(
            github.OrganizationDependabotAlert.OrganizationDependabotAlert,
            self._requester,
            f"{self.url}/dependabot/alerts",
            url_parameters,
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "avatar_url" in attributes:  # pragma no branch
            self._avatar_url = self._makeStringAttribute(attributes["avatar_url"])
        if "billing_email" in attributes:  # pragma no branch
            self._billing_email = self._makeStringAttribute(attributes["billing_email"])
        if "blog" in attributes:  # pragma no branch
            self._blog = self._makeStringAttribute(attributes["blog"])
        if "collaborators" in attributes:  # pragma no branch
            self._collaborators = self._makeIntAttribute(attributes["collaborators"])
        if "company" in attributes:  # pragma no branch
            self._company = self._makeStringAttribute(attributes["company"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "default_repository_permission" in attributes:  # pragma no branch
            self._default_repository_permission = self._makeStringAttribute(attributes["default_repository_permission"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "disk_usage" in attributes:  # pragma no branch
            self._disk_usage = self._makeIntAttribute(attributes["disk_usage"])
        if "email" in attributes:  # pragma no branch
            self._email = self._makeStringAttribute(attributes["email"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "followers" in attributes:  # pragma no branch
            self._followers = self._makeIntAttribute(attributes["followers"])
        if "following" in attributes:  # pragma no branch
            self._following = self._makeIntAttribute(attributes["following"])
        if "gravatar_id" in attributes:  # pragma no branch
            self._gravatar_id = self._makeStringAttribute(attributes["gravatar_id"])
        if "has_organization_projects" in attributes:  # pragma no branch
            self._has_organization_projects = self._makeBoolAttribute(attributes["has_organization_projects"])
        if "has_repository_projects" in attributes:  # pragma no branch
            self._has_repository_projects = self._makeBoolAttribute(attributes["has_repository_projects"])
        if "hooks_url" in attributes:  # pragma no branch
            self._hooks_url = self._makeStringAttribute(attributes["hooks_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issues_url" in attributes:  # pragma no branch
            self._issues_url = self._makeStringAttribute(attributes["issues_url"])
        if "location" in attributes:  # pragma no branch
            self._location = self._makeStringAttribute(attributes["location"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "members_can_create_repositories" in attributes:  # pragma no branch
            self._members_can_create_repositories = self._makeBoolAttribute(
                attributes["members_can_create_repositories"]
            )
        if "members_url" in attributes:  # pragma no branch
            self._members_url = self._makeStringAttribute(attributes["members_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "owned_private_repos" in attributes:  # pragma no branch
            self._owned_private_repos = self._makeIntAttribute(attributes["owned_private_repos"])
        if "plan" in attributes:  # pragma no branch
            self._plan = self._makeClassAttribute(github.Plan.Plan, attributes["plan"])
        if "private_gists" in attributes:  # pragma no branch
            self._private_gists = self._makeIntAttribute(attributes["private_gists"])
        if "public_gists" in attributes:  # pragma no branch
            self._public_gists = self._makeIntAttribute(attributes["public_gists"])
        if "public_members_url" in attributes:  # pragma no branch
            self._public_members_url = self._makeStringAttribute(attributes["public_members_url"])
        if "public_repos" in attributes:  # pragma no branch
            self._public_repos = self._makeIntAttribute(attributes["public_repos"])
        if "repos_url" in attributes:  # pragma no branch
            self._repos_url = self._makeStringAttribute(attributes["repos_url"])
        if "total_private_repos" in attributes:  # pragma no branch
            self._total_private_repos = self._makeIntAttribute(attributes["total_private_repos"])
        if "two_factor_requirement_enabled" in attributes:  # pragma no branch
            self._two_factor_requirement_enabled = self._makeBoolAttribute(attributes["two_factor_requirement_enabled"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
