class SynchrotronSelfComptonModel:
    """Model for synchrotron self-Compton scenario."""

    def __new__(cls, n_e, ssa=False, backend="gammapy"):
        if backend == "sherpa":
            try:
                from .sherpa_wrapper import SynchrotronSelfComptonRegriddableModel1D
            except ImportError:
                raise ImportError(
                    "sherpa is required to use the sherpa backend, "
                    "install it with: pip install sherpa"
                )
            return SynchrotronSelfComptonRegriddableModel1D(n_e, ssa)
        elif backend == "gammapy":
            try:
                from .gammapy_wrapper import SynchrotronSelfComptonSpectralModel
            except ImportError:
                raise ImportError(
                    "gammapy is required to use the gammapy backend, "
                    "install it with: pip install gammapy"
                )
            return SynchrotronSelfComptonSpectralModel(n_e, ssa)
        else:
            raise ValueError(
                f"{backend} is not an available backend, try gammapy or sherpa"
            )


class ExternalComptonModel:
    """Model for external Compton scenario."""

    def __new__(cls, n_e, targets, ssa=False, backend="gammapy"):
        if backend == "sherpa":
            try:
                from .sherpa_wrapper import ExternalComptonRegriddableModel1D
            except ImportError:
                raise ImportError(
                    "sherpa is required to use the sherpa backend, "
                    "install it with: pip install sherpa"
                )
            return ExternalComptonRegriddableModel1D(n_e, targets, ssa)
        elif backend == "gammapy":
            try:
                from .gammapy_wrapper import ExternalComptonSpectralModel
            except ImportError:
                raise ImportError(
                    "gammapy is required to use the gammapy backend, "
                    "install it with: pip install gammapy"
                )
            return ExternalComptonSpectralModel(n_e, targets, ssa)
        else:
            raise ValueError(
                f"{backend} is not an available backend, try gammapy or sherpa"
            )
