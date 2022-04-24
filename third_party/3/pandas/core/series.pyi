from __future__ import annotations

import collections
import sys
from io import StringIO
from typing import Any, Callable, Hashable, IO, Optional, Iterable, Union, Mapping, Sequence, Type, TypeVar, Dict, Set, \
    overload, DefaultDict

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

import numpy as np

from pandas._typing import ArrayLike as ArrayLike, OneDimensionalAxisOption, Column
from pandas._typing import Renamer, FrameOrSeries, Function, AxisOption, Frequency, Scalar, Dtype, \
    NoneNumpyCompatible, Level, \
    GroupByObject, GeneralDuplicatesKeepStrategy, Label, InterpolationMethod, CorrelationMethod, SearchSide, \
    SortKind, \
    AggregationFunction, JoinType, FillMethod, ErrorsStrategy, FillValue, ToReplace, ReplaceValue, \
    TimestampMethod, \
    ReplaceMethod, ValueKeyFunc, IndexKeyFunc
from pandas.core import base, generic
from pandas.core.arrays import ExtensionArray
from pandas.core.frame import DataFrame, KeepStrategy, TransformFunction
from pandas.core.groupby import generic as groupby_generic
from pandas.core.indexes.base import Index
from pandas.core.strings import StringMethods
from pandas.core.dates import DateTimeMethods

SortValuesNaPosition = Literal['first', 'last']
MapNaNAction = Literal['ignore']

# Only requirement for index is that it's hashable
ColumnMappingT = TypeVar("ColumnMappingT", bound=Mapping[Hashable, Any])


CoercibleIntoSeries = Union[Scalar, Dict[str, Scalar], Iterable[Scalar], ArrayLike]

class Series(base.IndexOpsMixin, generic.NDFrame):
    index: Index = ...
    # These are accessors and might need some work
    str: StringMethods = ...
    dt: DateTimeMethods = ...
    cat: Any = ...
    sparse: Any = ...
    plot: Any = ...
    hist: Any = ...
    def __init__(self, data: Optional[Any] = ..., index: Optional[Any] = ..., dtype: Optional[Dtype] = ..., name: Optional[Any] = ..., copy: bool = ..., fastpath: bool = ...) -> None: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: Label) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> Series: ...
    @overload
    def __setitem__(self, key: Label, value: Scalar) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Scalar) -> None: ...
    DotOther = Union['Series', DataFrame, ArrayLike]
    DotResult = Union[Scalar, 'Series', ArrayLike]
    @overload
    def __matmul__(self, other: DataFrame) -> Series: ...
    @overload
    def __matmul__(self, other: Series) -> Scalar: ...
    @overload
    def __matmul__(self, other: np.ndarray) -> np.ndarray: ...
    @overload
    def __rmatmul__(self, other: DataFrame) -> Series: ...  # type: ignore[misc]
    @overload
    def __rmatmul__(self, other: Series) -> Scalar: ...
    @overload
    def __rmatmul__(self, other: np.ndarray) -> np.ndarray: ...
    def __le__(self, other: Union[Scalar, Series]) -> Series: ...
    def __lt__(self, other: Union[Scalar, Series]) -> Series: ...
    def __ge__(self, other: Union[Scalar, Series]) -> Series: ...
    def __gt__(self, other: Union[Scalar, Series]) -> Series: ...
    def __mul__(self, other: Union[Scalar, Series]) -> Series: ...
    def __rmul__(self, other: Union[Scalar, Series]) -> Series: ...
    def __pow__(self, other: Union[Scalar, Series]) -> Series: ...
    def __add__(self, other: Union[Scalar, Series]) -> Series: ...
    def __radd__(self, other: Union[Scalar, Series]) -> Series: ...
    def __sub__(self, other: Union[Scalar, Series]) -> Series: ...
    def __rsub__(self, other: Union[Scalar, Series]) -> Series: ...
    def __truediv__(self, other: Union[Scalar, Series]) -> Series: ...
    def __rtruediv__(self, other: Union[Scalar, Series]) -> Series: ...
    def __floordiv__(self, other: Union[Scalar, Series]) -> Series: ...
    def __rfloordiv__(self, other: Union[Scalar, Series]) -> Series: ...
    def __mod__(self, other: Union[Scalar, Series]) -> Series: ...
    def __rmod__(self, other: Union[Scalar, Series]) -> Series: ...
    def __and__(self, other: Union[Scalar, Series]) -> Series: ...
    def __rand__(self, other: Union[Scalar, Series]) -> Series: ...
    def __or__(self, other: Union[Scalar, Series]) -> Series: ...
    def __ror__(self, other: Union[Scalar, Series]) -> Series: ...
    def __invert__(self) -> Series: ...
    def __eq__(self, other: Union[Scalar, Series]) -> Series: ...  # type: ignore
    def __ne__(self, other: Union[Scalar, Series]) -> Series: ...  # type: ignore
    @property
    def dtype(self) -> Dtype: ...
    @property
    def dtypes(self) -> Dtype: ...
    @property
    def name(self) -> Optional[Hashable]: ...
    @name.setter
    def name(self, value: Optional[Hashable]) -> None: ...
    @property
    def values(self) -> ArrayLike: ...
    @property
    def hasnans(self) -> bool: ...
    @property
    def array(self) -> ExtensionArray: ...
    def div(self,other: Union[Scalar, Series], axis: Optional[OneDimensionalAxisOption] = ...,level: Optional[Level] = ..., fill_value: Optional[Scalar] = ...,) -> Series: ...
    def rdiv(self,other: Union[Scalar, Series], axis: Optional[OneDimensionalAxisOption] = ...,level: Optional[Level] = ..., fill_value: Optional[Scalar] = ...,) -> Series: ...
    def ravel(self, order: str = ...) -> Any: ...
    def view(self, dtype: Optional[Dtype] = ...) -> Any: ...
    def __array_ufunc__(self, ufunc: Function, method: str, *inputs: Any, **kwargs: Any) -> Any: ...
    def __array__(self, dtype: Any = ...) -> np.ndarray: ...
    @property
    def axes(self) -> Any: ...
    def take(self, indices: Union[Iterable[int], np.ndarray[np.int_]], axis: AxisOption = ..., is_copy: bool = ..., **kwargs: Any) -> Series: ...
    def repeat(self, repeats: Union[int, Iterable[int]], axis: Optional[NoneNumpyCompatible] = ...) -> Series: ...
    @overload
    def reset_index(self, level: Optional[Level] = ..., drop: bool = ..., name: Optional[Any] = ..., *, inplace: Literal[False] = ...) -> FrameOrSeries: ...
    @overload
    def reset_index(self, level: Optional[Level] = ..., drop: bool = ..., name: Optional[Any] = ..., *, inplace: Literal[True]) -> None: ...
    def to_string(self, buf: Optional[StringIO] = ..., na_rep: Optional[str] = ..., float_format: Optional[Callable[[Any], Any]] = ..., header: bool = ..., index: bool = ..., length: bool = ..., dtype: bool = ..., name: bool = ..., max_rows: Optional[int] = ..., min_rows: Optional[int] = ...) -> Union[str, None]: ...
    def to_markdown(self, buf: Optional[IO[str]]=..., mode: Optional[str]=..., index: bool = ..., **kwargs: Any) -> Optional[str]: ...
    def items(self) -> Iterable[Any]: ...
    def iteritems(self) -> Iterable[Any]: ...
    def keys(self) -> Index: ...
    # Dict is the default type if not specified - haven't used default argument because Type didn't work with generic
    @overload
    def to_dict(self) -> Dict[Hashable, Any]: ...
    @overload
    def to_dict(self, into: Type[ColumnMappingT]) -> ColumnMappingT: ...
    # collections.defaultdict is a special case - it's passed as initialized
    @overload
    def to_dict(self, into: DefaultDict[Hashable, Any]) -> DefaultDict[Hashable, Any]: ...
    def to_frame(self, name: Optional[Any] = ...) -> DataFrame: ...
    def groupby(self, by: Optional[GroupByObject] = ..., axis: AxisOption = ..., level: Optional[Union[Level, Iterable[Level]]] = ..., as_index: bool=..., sort: bool=..., group_keys: bool=..., squeeze: bool=..., observed: bool=..., dropna: bool=...) -> groupby_generic.SeriesGroupBy: ...
    def count(self, level: Optional[Level] = ...) -> Union[int, Series]: ...
    def mode(self, dropna: bool = ...) -> Series: ...
    def unique(self) -> ArrayLike: ...
    @overload
    def drop_duplicates(self, keep: GeneralDuplicatesKeepStrategy = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def drop_duplicates(self, keep: GeneralDuplicatesKeepStrategy = ..., *, inplace: Literal[True]) -> None: ...
    def duplicated(self, keep: GeneralDuplicatesKeepStrategy = ...) -> Series: ...
    def idxmin(self, axis: int = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Label: ...
    def idxmax(self, axis: int = ..., skipna: bool = ..., *args: Any, **kwargs: Any) -> Label: ...
    def round(self, decimals: int = ..., *args: Any, **kwargs: Any) -> Series: ...
    def quantile(self, q: Union[float, ArrayLike] = ..., interpolation: InterpolationMethod = ...) -> Union[float, Series]: ...
    def corr(self, other: Series, method: CorrelationMethod = ..., min_periods: Optional[int] = ...) -> float: ...
    def cov(self, other: Series, min_periods: Optional[int] = ..., ddof: Optional[int] = ...) -> float: ...
    def diff(self, periods: int = ...) -> Series: ...
    def autocorr(self, lag: int = ...) -> float: ...
    @overload
    def dot(self, other: DataFrame) -> Series: ...
    @overload
    def dot(self, other: Series) -> Scalar: ...
    @overload
    def dot(self, other: np.ndarray) -> np.ndarray: ...
    def all(self,axis: AxisOption = ..., bool_only: Optional[bool] = ..., skipna: bool = ..., level: Optional[Level] = ..., **kwargs: Any) -> bool: ...
    def any(self,axis: AxisOption = ..., bool_only: Optional[bool] = ..., skipna: bool = ..., level: Optional[Level] = ..., **kwargs: Any) -> bool: ...
    def searchsorted(self, value: ArrayLike, side: SearchSide = ..., sorter: Optional[ArrayLike] = ...) -> Sequence[int]: ...   # type: ignore[override]
    def append(self, to_append: Union[Series, Iterable[Series]], ignore_index: bool = ..., verify_integrity: bool = ...) -> Series: ...
    def combine(self, other: Union[Series, Scalar], func: Callable[[Scalar, Scalar], Scalar], fill_value: Optional[Scalar] = ...) -> Series: ...
    def combine_first(self, other: Series) -> Series: ...
    def update(self, other: Union[Series, CoercibleIntoSeries]) -> None: ...
    @overload    # type: ignore[override]
    def sort_values(self, axis: OneDimensionalAxisOption = ..., ascending: bool = ..., kind: SortKind = ..., na_position: SortValuesNaPosition = ..., ignore_index: bool = ..., key: ValueKeyFunc = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def sort_values(self, axis: OneDimensionalAxisOption = ..., ascending: bool = ..., kind: SortKind = ..., na_position: SortValuesNaPosition = ..., ignore_index: bool = ..., key: ValueKeyFunc = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def sort_index(self, axis: int = ..., level: int = ..., ascending: Union[bool, Iterable[bool]] = ..., kind: SortKind = ..., na_position: SortValuesNaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ..., *,  inplace: Literal[False] = ...) -> Series: ...
    @overload
    def sort_index(self, axis: int = ..., level: int = ..., ascending: Union[bool, Iterable[bool]] = ..., kind: SortKind = ..., na_position: SortValuesNaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ..., *,  inplace: Literal[True]) -> None: ...
    def argsort(self, axis: OneDimensionalAxisOption = ..., kind: SortKind = ..., order: Optional[Any] = ...) -> Series: ...
    def nlargest(self, n: int = ..., keep: KeepStrategy = ...) -> Series: ...
    def nsmallest(self, n: int = ..., keep: KeepStrategy = ...) -> Series: ...
    def swaplevel(self, i: int = ..., j: int = ..., copy: bool = ...) -> Series: ...
    def reorder_levels(self, order: Iterable[int]) -> Series: ...
    def explode(self) -> Series: ...
    def unstack(self, level: Union[Level, Iterable[Level]] = ..., fill_value: Optional[Scalar] = ...) -> DataFrame: ...
    def map(self, arg: Union[Function, collections.abc.Mapping[Any, Any], Series], na_action: Optional[MapNaNAction] = ...) -> Series: ...
    def aggregate(self, func: AggregationFunction = ..., axis: OneDimensionalAxisOption = ..., *args: Any, **kwargs: Any) -> FrameOrSeries: ...
    def agg(self, func: AggregationFunction = ..., axis: OneDimensionalAxisOption = ..., *args: Any, **kwargs: Any) -> FrameOrSeries: ...
    def transform(self, func: TransformFunction, axis: OneDimensionalAxisOption = ..., *args: Any, **kwargs: Any) -> Series: ...
    def apply(self, func: Function, convert_dtype: bool = ..., args: Any = ..., **kwds: Any) -> FrameOrSeries: ...
    def align(self, other: FrameOrSeries, join: JoinType = ..., axis: Optional[OneDimensionalAxisOption] = ..., level: Optional[Level] = ..., copy: bool = ..., fill_value: Optional[Scalar] = ..., method: Optional[FillMethod] = ..., limit: Optional[int] = ..., fill_axis: OneDimensionalAxisOption = ..., broadcast_axis: Optional[OneDimensionalAxisOption] = ...) -> Series: ...  # type: ignore
    @overload  #type: ignore[override]
    def rename(self, index: Optional[Union[Renamer, Scalar, Hashable]] = ..., *, axis: Optional[OneDimensionalAxisOption] = ..., copy: bool = ..., inplace: Literal[False] = ..., level: Optional[Level] = ..., errors: ErrorsStrategy = ...) -> Series: ...
    @overload
    def rename(self, index: Optional[Union[Renamer, Scalar, Hashable]] = ..., *, axis: Optional[OneDimensionalAxisOption] = ..., copy: bool = ..., inplace: Literal[True], level: Optional[Level] = ..., errors: ErrorsStrategy = ...) -> None: ...
    def reindex(self, index: Optional[Union[Label, Iterable[Label]]] = ..., **kwargs: Any) -> FrameOrSeries: ... # type: ignore[override]
    @overload
    def drop(self, labels: Optional[Union[Label, Iterable[Label]]] = ..., axis: OneDimensionalAxisOption = ..., index: Optional[Union[Label, Iterable[Label]]]  = ..., columns: Optional[Union[Label, Iterable[Label]]]  = ..., level: Optional[Level] = ..., errors: ErrorsStrategy = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def drop(self, labels: Optional[Union[Label, Iterable[Label]]] = ..., axis: OneDimensionalAxisOption = ..., index: Optional[Union[Label, Iterable[Label]]]  = ..., columns: Optional[Union[Label, Iterable[Label]]]  = ..., level: Optional[Level] = ..., errors: ErrorsStrategy = ...,*, inplace: Literal[True]) -> None: ...
    @overload
    def fillna(self, value: FillValue = ..., method: FillMethod = ..., axis: OneDimensionalAxisOption = ..., limit: int = ..., downcast: Dict[Any, Dtype] = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def fillna(self, value: FillValue = ..., method: FillMethod = ..., axis: OneDimensionalAxisOption = ..., limit: int = ..., downcast: Dict[Any, Dtype] = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def bfill(self, axis: OneDimensionalAxisOption = ..., limit: int = ..., downcast: Dict[Any, Dtype] = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def bfill(self, axis: OneDimensionalAxisOption = ...,limit: int = ..., downcast: Dict[Any, Dtype] = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def ffill(self, axis: Any = ..., limit: Any = ..., downcast: Any = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def ffill(self, axis: Any = ..., limit: Any = ..., downcast: Any = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def replace(self, to_replace: Optional[ToReplace] = ..., value: Optional[ReplaceValue] = ..., limit: Optional[int] = ..., regex: bool = ..., method: ReplaceMethod = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def replace(self, to_replace: Optional[ToReplace] = ..., value: Optional[ReplaceValue] = ..., limit: Optional[int] = ..., regex: bool = ..., method: ReplaceMethod = ..., *, inplace: Literal[True]) -> None: ...
    def shift(self, periods: int = ..., freq: Optional[Frequency] = ..., axis: AxisOption = ..., fill_value: Scalar = ...) -> Series: ...
    def memory_usage(self, index: bool = ..., deep: bool = ...) -> int: ... # type: ignore[override]
    def isin(self, values: Union[Set[Scalar], Iterable[Scalar]]) -> Series: ...
    def between(self, left: Union[Scalar, Iterable[Scalar]], right: Union[Scalar, Iterable[Scalar]], inclusive: bool = ...) -> Series: ...
    def isna(self) -> Series: ...
    def isnull(self) -> Series: ...
    def notna(self) -> Series: ...
    def notnull(self) -> Series: ...
    @overload
    def dropna(self, axis: OneDimensionalAxisOption = ..., how: Optional[Any] = ..., *, inplace: Literal[False] = ...) -> Series: ...
    @overload
    def dropna(self, axis: OneDimensionalAxisOption = ..., how: Optional[Any] = ..., *, inplace: Literal[True]) -> None: ...
    def to_timestamp(self, freq: Optional[str] = ..., how: TimestampMethod = ..., copy: bool = ...) -> Series: ...
    def to_period(self, freq: Optional[str] = ..., copy: bool = ...) -> Series: ...
    def compare(self, other: Series, align_axis: AxisOption = ..., keep_shape: bool = ..., keep_equal: bool = ...) -> FrameOrSeries: ...
    @overload
    def median(self, axis: Optional[AxisOption] = ..., skipna: Optional[bool] = ..., level: None = ..., numeric_only: Optional[bool] = ..., **kwargs: Any) -> float: ...
    @overload
    def median(self, axis: Optional[AxisOption], skipna: Optional[bool], level: Union[Hashable, int], numeric_only: Optional[bool] = ..., **kwargs: Any) -> Series: ...
    @overload
    def median(self, axis: Optional[AxisOption], level: Union[Hashable, int], numeric_only: Optional[bool] = ..., **kwargs: Any) -> Series: ...
    @overload
    def median(self, level: Union[Hashable, int], numeric_only: Optional[bool] = ..., **kwargs: Any) -> Series: ...
    @overload
    def mean(self, axis: Optional[AxisOption] = ..., skipna: Optional[bool] = ..., level: None = ..., numeric_only: Optional[bool] = ..., **kwargs: Any) -> float: ...
    @overload
    def mean(self, axis: Optional[AxisOption], skipna: Optional[bool], level: Union[Hashable, int], numeric_only: Optional[bool] = ..., **kwargs: Any) -> Series: ...
    @overload
    def mean(self, axis: Optional[AxisOption], level: Union[Hashable, int], numeric_only: Optional[bool] = ..., **kwargs: Any) -> Series: ...
    @overload
    def mean(self, level: Union[Hashable, int], numeric_only: Optional[bool] = ..., **kwargs: Any) -> Series: ...
    def astype(self, dtype: Any, copy: bool = ..., errors: str = ...) -> Series: ...
