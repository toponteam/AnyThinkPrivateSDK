#
# Be sure to run `pod lib lint TopOnPrivateSDK.podspec' to ensure this is a
# valid spec before submitting.
#
# Any lines starting with a # are optional, but their use is encouraged
# To learn more about a Podspec see https://guides.cocoapods.org/syntax/podspec.html
#

  Pod::Spec.new do |s|
  s.name             = 'AnyThinkPrivateSDK'
  s.version          = '1.1.0'
  s.summary          = 'AnyThinkPrivate'
  s.description      = <<-DESC
      AnyThinkPrivateSDK,Vungle,Kidoz,Ogury,Appnext
                       DESC
  s.homepage         = 'https://github.com/toponteam/AnyThinkPrivateSDK.git'
  s.license          = { :type => 'MIT', :file => 'LICENSE' }
  s.author           = { 'GUO PENG' => 'ios' }
  s.source           = { :git => 'https://github.com/toponteam/AnyThinkPrivateSDK.git', :tag => s.version.to_s }
  
  s.ios.deployment_target = '9.0'
  
  s.requires_arc = true

  s.frameworks = 'SystemConfiguration', 'CoreGraphics','Foundation','UIKit'
  
  s.pod_target_xcconfig =   {'OTHER_LDFLAGS' => ['-lObjC']}
  
  s.libraries = 'c++', 'z', 'sqlite3', 'xml2', 'resolv'
  
  s.pod_target_xcconfig = { 'VALID_ARCHS' => 'x86_64 armv7 armv7s arm64' }

    s.subspec 'ATPangleAdapter' do |ss|
    ss.ios.deployment_target = '9.0'
    ss.dependency 'Ads-Global-Beta','4.1.0.0'
    ss.dependency 'AnyThinkiOS/AnyThinkSDK','5.7.81'
    ss.vendored_frameworks = 'Adapters/AnyThinkPangleAdapter.framework'
    
  end
  
    s.subspec 'ATTTAdapter' do |ss|
    ss.ios.deployment_target = '9.0'
    ss.vendored_frameworks = 'Adapters/AnyThinkTTAdapter.framework'
    ss.dependency 'Ads-CN-Beta','4.1.0.0'
    ss.dependency 'AnyThinkiOS/AnyThinkSDK','5.7.81'
  end

end
