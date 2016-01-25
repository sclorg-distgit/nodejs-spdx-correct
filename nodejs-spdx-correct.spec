%{?scl:%scl_package nodejs-spdx-correct}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-spdx-correct

%global npm_name spdx-correct
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-spdx-correct
Version:	1.0.2
Release:	1%{?dist}
Summary:	correct invalid SPDX identifiers
Url:		https://github.com/kemitchell/spdx-correct.js#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	Apache-2.0

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(defence-cli)
BuildRequires:	%{?scl_prefix}npm(replace-require-self)
BuildRequires:	%{?scl_prefix}npm(spdx-expression-parse)
BuildRequires:	%{?scl_prefix}npm(tape)
%endif

BuildRequires:	%{?scl_prefix}npm(spdx-license-ids)

Requires:	%{?scl_prefix}npm(spdx-license-ids)

%description
correct invalid SPDX identifiers

%prep
%setup -q -n package
%nodejs_fixdep spdx-license-ids '>=1.0.1'
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/spdx-correct

%doc README.md
%doc LICENSE

%changelog
* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-1
- Initial build
