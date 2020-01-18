Name:           plexus-cipher
Version:        1.7
Release:        5%{?dist}
Summary:        Plexus Cipher: encryption/decryption Component

License:        ASL 2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/sonatype/plexus-cipher
# git clone https://github.com/sonatype/plexus-cipher.git
# cd plexus-cipher/
# note this is version 1.7 + our patches which were incorporated by upstream maintainer
# git archive --format tar --prefix=plexus-cipher-1.7/ 0cff29e6b2e | gzip -9 > plexus-cipher-1.7.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: forge-parent
BuildRequires: spice-parent
BuildRequires: plexus-containers-component-metadata
BuildRequires: junit
BuildRequires: maven-shared-reporting-impl
BuildRequires: plexus-digest
BuildRequires: sisu-maven-plugin
BuildRequires: sisu-inject-bean

Requires: jpackage-utils
Requires: java


%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_replace pom:project/pom:version "<version>%{version}</version>"

%mvn_file : plexus/%{name}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.7-5
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7-4
- Migrate away from mvn-rpmbuild (#997451)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 13 2013 Michal Srb <msrb@redhat.com> - 1.7-1
- Update to upstream version 1.7

* Thu Feb 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-15
- Reemove BR: plexus-container-default

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 1.5-14
- Remove unnecessary dependency on plexus-containers (#908586)

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.5-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 02 2013 Michal Srb <msrb@redhat.com> - 1.5-12
- Fixed URL (Resolves: #880322)

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-11
- Improve randomness of PBECipher
- Resolves: rhbz#880279

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-10
- Remove duplicated NOTICE file

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-9
- Add ASL 2.0 text and install NOTICE file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 1.5-6
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-5
- Do not require maven2.
- Build with maven (v. 3) by default.
- drop obsoleted parts of the spec.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Hui Wang <huwang@redhat.com> - 1.5-3
- Add NOTICE.text
- Fix URL
- Fix direction of install pom

* Sun May 23 2010 Hui Wang <huwang@redhat.com> - 1.5-2
- Correct URL

* Tue May 18 2010 Hui Wang <huwang@redhat.com> - 1.5-1
- Initial version of the package
