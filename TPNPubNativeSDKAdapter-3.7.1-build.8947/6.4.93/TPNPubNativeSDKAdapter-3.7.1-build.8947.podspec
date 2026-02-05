#
# Be sure to run `pod lib lint TPNPubNativeAdapter.podspec' to ensure this is a
# valid spec before submitting.
#
# Any lines starting with a # are optional, but their use is encouraged
# To learn more about a Podspec see https://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|
  s.name             = 'TPNPubNativeSDKAdapter-3.7.1-build.8947'
  s.version          = '6.4.93'
  s.summary          = 'TPNPubNativeAdapter used for mediation with the TopOn SDK'

  s.description      = <<-DESC
     TopOn SDK for developer
                       DESC

  s.homepage = 'https://www.toponad.com'
  s.author = { 'topon' => 'mct-js@toponad.com' }
  s.license = { :type => "MIT" }

  s.ios.deployment_target = '12.0'
  s.static_framework = true
  s.requires_arc = true
  s.pod_target_xcconfig = {
    'OTHER_LDFLAGS' => ['-lObjC'],
    'VALID_ARCHS' => 'armv7 arm64'
  }

  s.source = {
    :http => "https://topon-sdk-release.oss-cn-hangzhou.aliyuncs.com/TPN_Release/v6.4.93/iOS/TPN_mediation/AnyThinkPubNativeAdapter-6.4.93.8.zip",
    :type => 'zip'
  }
  s.vendored_frameworks = "AnyThinkPubNativeAdapter-6.4.93.8/AnyThinkPubNativeAdapter.xcframework"

  s.dependency 'TPNiOS','6.4.93'
  s.dependency 'HyBid-private', '3.7.1-build.8947'

  
end
