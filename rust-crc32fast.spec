# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate crc32fast

Name:           rust-crc32fast
Version:        1.4.0
Release:        1
Summary:        Fast, SIMD-accelerated CRC32 (IEEE) checksum computation
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crc32fast
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0~)
%if %{with check}
BuildRequires:  (crate(bencher/default) >= 0.1.0 with crate(bencher/default) < 0.2.0~)
BuildRequires:  (crate(quickcheck) >= 1.0.0 with crate(quickcheck) < 2.0.0~)
BuildRequires:  (crate(rand/default) >= 0.8.0 with crate(rand/default) < 0.9.0~)
%endif

%global _description %{expand:
Fast, SIMD-accelerated CRC32 (IEEE) checksum computation.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(crc32fast) = 1.4.0
Requires:       (crate(cfg-if/default) >= 1.0.0 with crate(cfg-if/default) < 2.0.0~)
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(crc32fast/default) = 1.4.0
Requires:       cargo
Requires:       crate(crc32fast) = 1.4.0
Requires:       crate(crc32fast/std) = 1.4.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(crc32fast/nightly) = 1.4.0
Requires:       cargo
Requires:       crate(crc32fast) = 1.4.0

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(crc32fast/std) = 1.4.0
Requires:       cargo
Requires:       crate(crc32fast) = 1.4.0

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
